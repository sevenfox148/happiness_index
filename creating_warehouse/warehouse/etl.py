import pandas as pd
from sqlalchemy import create_engine
import pg8000
import numpy as np
import country_converter as coco

engine = create_engine("postgresql+pg8000://postgres:62951413Pie@localhost:5432/Happiness_index")
schema1 = 'stage_zone'
schema2 = 'warehouse'

# read dataframes from stage zone
happiness = pd.read_sql_table('world_happiness', engine, schema=schema1)
freedom = pd.read_sql_table('world_freedom', engine, schema=schema1)
economic_freedom = pd.read_sql_table('world_economic_freedom', engine, schema=schema1)

# drop duplicates on [year, country] subset
happiness.sort_values(by='life_ladder', ascending=False, inplace=True)
happiness.drop_duplicates(subset=['year', 'country_name'], keep='first', inplace=True)
happiness.sort_index(inplace=True)

freedom.sort_values(by=['total'], ascending=False, inplace=True)
freedom.drop_duplicates(subset=['edition', 'country'], keep='first', inplace=True)
freedom.sort_index(inplace=True)

economic_freedom.sort_values(by='summary_index', ascending=False, inplace=True)
economic_freedom.drop_duplicates(subset=['research_year', 'country'], keep='first', inplace=True)
economic_freedom.sort_index(inplace=True)

# filling nulls with average
column_not_fill = [['country_name', 'year', 'life_ladder'],
                   ['country', 'edition', 'region', 'status', 'total'],
                   ['country', 'research_year', 'bank_region', 'income_classification', 'summary_index']]


def fill_null(df, not_fill_num, db_table, country, year):
    for column in df.columns:
        if column not in column_not_fill[not_fill_num]:
            if df[column].dtype == 'int64' or df[column].dtype == 'float64':

                avg_by_country = pd.read_sql_query(f"""
                SELECT  
                    AVG({column}) OVER (PARTITION BY {country} ORDER BY {year}) AS avg_value
                FROM 
                    {schema1}.{db_table};
            """, engine)

                df[column] = df[column].fillna(avg_by_country['avg_value'])

                df[column] = df[column].apply(lambda x: abs(x) if x < 0 else x)


fill_null(happiness, 0, 'world_happiness', 'country_name', 'year')
fill_null(freedom, 1, 'world_freedom', 'country', 'edition')
fill_null(economic_freedom, 2, 'world_economic_freedom', 'country', 'research_year')

# drop nulls in dim columns
happiness.dropna(subset=column_not_fill[0], inplace=True)
freedom.dropna(subset=column_not_fill[1], inplace=True)
economic_freedom.dropna(subset=column_not_fill[2], inplace=True)

# change '..' to NaN
economic_freedom['income_classification'] = economic_freedom['income_classification'].replace('..', np.nan)

# normalizing country names
cc = coco.CountryConverter()
freedom = freedom[freedom.ct == 'c']
happiness['country_name'] = happiness['country_name'].apply(lambda x: cc.convert(names=x, to='name_short'))
freedom['country'] = freedom['country'].apply(lambda x: cc.convert(names=x, to='name_short'))
economic_freedom['country'] = economic_freedom['country'].apply(lambda x: cc.convert(names=x, to='name_short'))

# joining information about countries
countries_info = pd.DataFrame(pd.unique(pd.concat([happiness['country_name'], freedom['country'],
                                                   economic_freedom['country']])))
countries_info.columns = ['country']

uniq_economic_countries = economic_freedom.drop_duplicates(subset=['country'],
                                                           keep='first')[['country', 'bank_region', 'iso2', 'iso3']]
uniq_economic_countries = uniq_economic_countries.set_index('country')
countries_info = pd.merge(countries_info, uniq_economic_countries[['bank_region', 'iso2', 'iso3']], left_on='country',
                          right_on='country', how='left')

uniq_freedom_countries = freedom.drop_duplicates(subset=['country'], keep='first')[['country','region']]
uniq_freedom_countries = uniq_freedom_countries.set_index('country')
countries_info = pd.merge(countries_info, uniq_freedom_countries, left_on='country', right_index=True, how='left')

# normalize region, iso2, iso3
countries_info['iso2'] = countries_info.apply(lambda row: cc.convert(names=row['country'], to='ISO2'), axis=1)
countries_info['iso3'] = countries_info.apply(lambda row: cc.convert(names=row['country'], to='ISO3'), axis=1)
countries_info['region'] = countries_info.apply(lambda row: cc.convert(names=row['country'], to='continent'), axis=1)
countries_info = countries_info.set_index('iso2')

# select unique bank regions
bank_region_info = countries_info.drop_duplicates(subset=['bank_region'], keep='first')[['bank_region']]
bank_region_info.dropna(subset='bank_region', inplace=True)
bank_region_info = bank_region_info.reset_index(drop=True)
bank_region_info.index = bank_region_info.index + 1

# select unique regions
region_info = countries_info.drop_duplicates(subset=['region'], keep='first')[['region']]
region_info = region_info.reset_index(drop=True)
region_info.dropna(subset='region', inplace=True)
region_info.index = region_info.index + 1

# replace regions with ids
countries_info['bank_region'] = countries_info['bank_region'].apply(lambda x: int(bank_region_info.index[bank_region_info['bank_region'] == x].tolist()[0]) if not pd.isnull(x) else np.nan)
countries_info['region'] = countries_info['region'].apply(lambda x: int(region_info.index[region_info['region'] == x].tolist()[0]) if not pd.isnull(x) else np.nan)

# select unique years
date_info = pd.DataFrame(pd.unique(pd.concat([happiness['year'], freedom['edition'], economic_freedom['research_year']])))
date_info.columns = ['year']

# select unique statuses
freedom_status = pd.DataFrame(freedom['status'])
freedom_status.drop_duplicates(keep='first', inplace=True)
bank_region_info.dropna(inplace=True)

# select unique income classifications
income_class = pd.DataFrame(economic_freedom['income_classification'])
income_class.drop_duplicates(keep='first', inplace=True)
income_class.dropna(inplace=True)
income_class.columns = ['income_class']

# create fact tables and change country to iso2
fact_happiness = happiness.drop(columns=['regional_indicator'])
fact_happiness.columns = ['country', 'year', 'index', 'gdp_per_capita', 'soc_support', 'life_expectancy',
                          'freedom', 'generosity', 'corruption', 'positive_affect', 'negative_affect', 'government']

fact_happiness['country'] = fact_happiness['country'].apply(lambda x: countries_info.index[countries_info['country'] == x].tolist()[0])


fact_freedom = freedom.drop(columns=['pr_rating', 'cl_rating', 'region','ct'])
fact_freedom.columns = ['country', 'year', 'status', 'electoral_process', 'pluralism', 'gov_functioning', 'pol_rights',
                        'belief_freedom', 'organizations', 'law', 'individual', 'civil_liberties', 'total']

fact_freedom['country'] = fact_freedom['country'].apply(lambda x: countries_info.index[countries_info['country'] == x].tolist()[0])


fact_econ_freedom = economic_freedom.drop(columns=['freedom_rank', 'gender_disparity', 'legal_index_gendered',
                                                   'iso3', 'iso2', 'bank_region'])
fact_econ_freedom.columns = ['year', 'country', 'index', 'government_index', 'legal_index', 'sound_money',
                             'international_trade', 'regulations', 'income_class']
fact_econ_freedom['country'] = fact_econ_freedom['country'].apply(lambda x: countries_info.index[countries_info['country'] == x].tolist()[0])


# write dataframes to warehouse
bank_region_info.to_sql('dim_bank_region', engine, if_exists='append', index=False, schema=schema2)
region_info.to_sql('dim_region', engine, if_exists='append', index=False, schema=schema2)
countries_info.to_sql('dim_country', engine, if_exists='append', index=True, schema=schema2)
date_info.to_sql('dim_date', engine, if_exists='append', index=False, schema=schema2)
freedom_status.to_sql('dim_freedom_status', engine, if_exists='append', index=False, schema=schema2)
income_class.to_sql('dim_income_class', engine, if_exists='append', index=False, schema=schema2)
fact_happiness.to_sql('fact_happiness', engine, if_exists='append', index=False, schema=schema2)
fact_freedom.to_sql('fact_pol_freedom', engine, if_exists='append', index=False, schema=schema2)
fact_econ_freedom.to_sql('fact_econ_freedom', engine, if_exists='append', index=False, schema=schema2)