import pandas as pd
from sqlalchemy import create_engine
import sys

engine = create_engine("postgresql+pg8000://postgres:62951413Pie@localhost:5432/Happiness_index")
schema = 'stage_zone'

economic_freedom_file = '../../data/world_economic_freedom.csv'
political_freedom_file = '../../data/world_freedom.csv'
happiness_file = '../../data/world_happiness_report.csv'

economic_freedom_db = 'world_economic_freedom'
political_freedom_db = 'world_freedom'
happiness_db = 'world_happiness'

type_mapping = {
    'numeric': 'float64',
    'decimal': 'float64',
    'character': 'object',
    'character varying': 'object',
    'integer': 'int64'
}


def check_types(dataframe: pd.DataFrame, table_name: str) -> None:

    pandas_types = dataframe.dtypes.astype(str).to_dict()

    query = (f"SELECT column_name, data_type FROM information_schema.columns WHERE table_schema = '{schema}' "
             f"AND table_name = '{table_name}';")
    db_types = pd.read_sql(query, engine)
    db_types = db_types.set_index('column_name')['data_type']
    db_types = db_types.to_dict()

    for column, pandas_type in pandas_types.items():
        db_type = db_types.get(column, None)
        if db_type is None:
            sys.exit(f"Column {column} not found in table {table_name}.")
        else:
            # Перевірка відповідності типів
            if type_mapping.get(db_type, None) != pandas_type:
                sys.exit(f"Types of column {column} don't match\npandas: {pandas_type}\ntable: {db_type}.")


# Economic freedom index
economic_freedom = pd.read_csv(economic_freedom_file, skiprows=4)
economic_freedom.rename(columns={economic_freedom.columns[0]: "null"}, inplace=True)
economic_freedom.drop(columns=['null'], inplace=True)

save_columns = economic_freedom.columns[economic_freedom.columns.str.contains(r'^\d+ ', regex=True)]
save_columns = save_columns.append(economic_freedom.columns
                                   [economic_freedom.columns.str.contains(r'ISO', regex=True)])
save_columns = save_columns.append(economic_freedom.columns
                                   [economic_freedom.columns.str.contains(r'Gender', regex=True)])
save_columns = save_columns.append(economic_freedom.columns
                                   [economic_freedom.columns.str.contains(r'World Bank', regex=True)])
save_columns = save_columns.append(pd.Index(['Year', 'Countries', 'Economic Freedom Summary Index', 'Rank']))
save_columns = pd.Index(set(save_columns))

save_columns = economic_freedom.columns.intersection(save_columns)
economic_freedom = economic_freedom[save_columns]

economic_freedom.columns = ['research_year', 'iso2', 'iso3', 'country', 'summary_index',
                            'freedom_rank', 'government_index', 'gender_disparity', 'legal_index_gendered',
                            'legal_index', 'sound_money', 'international_trade', 'regulations', 'bank_region',
                            'income_classification']

check_types(economic_freedom, economic_freedom_db)

# Political freedom index
political_freedom = pd.read_csv(political_freedom_file)
delete_columns = political_freedom.columns[political_freedom.columns.str.contains(r'[A-Z]\d+', regex=True)]
political_freedom.drop(columns=delete_columns, inplace=True)
political_freedom.columns = [col.lower().replace(' ', '_') for col in political_freedom.columns]
check_types(political_freedom, political_freedom_db)


# Happiness index
happiness = pd.read_csv('../../data/world_happiness_report.csv')
happiness.columns = [col.lower().replace(' ', '_') for col in happiness.columns]
check_types(happiness, happiness_db)


economic_freedom.to_sql(economic_freedom_db, engine, if_exists='append', index=False, schema=schema)
political_freedom.to_sql(political_freedom_db, engine, if_exists='append', index=False, schema='stage_zone')
happiness.to_sql(happiness_db, engine, if_exists='append', index=False, schema='stage_zone')
#%%
