CREATE SCHEMA stage_zone;

CREATE TABLE stage_zone.world_happiness(
	country_name VARCHAR(30),
	regional_indicator VARCHAR,
	year INTEGER,
	life_ladder NUMERIC,
	log_gdp_per_capita NUMERIC,
	social_support NUMERIC,
	healthy_life_expectancy_at_birth NUMERIC,
	freedom_to_make_life_choices NUMERIC,
	generosity NUMERIC,
	perceptions_of_corruption NUMERIC,
	positive_affect NUMERIC,
	negative_affect NUMERIC,
	confidence_in_national_government NUMERIC
);

CREATE TABLE stage_zone.world_freedom(
	country VARCHAR(30),
	region VARCHAR,
	ct CHAR(1),
    edition INTEGER,
	status VARCHAR(2),
	pr_rating INTEGER,
	cl_rating INTEGER,
	a INTEGER,
	b INTEGER,
	c INTEGER,
	pr INTEGER,
	d INTEGER,
	e INTEGER,
	f INTEGER,
	g INTEGER,
	cl INTEGER,
	total INTEGER
);

CREATE TABLE stage_zone.world_economic_freedom(
	research_year INTEGER,
	iso2 CHAR(2),
	iso3 CHAR(3),
	country VARCHAR(30),
	summary_index NUMERIC,
	freedom_rank NUMERIC,
	government_index NUMERIC,
	gender_disparity NUMERIC,
	legal_index_gendered NUMERIC,
	legal_index NUMERIC,
	sound_money NUMERIC,
	international_trade NUMERIC,
	regulations NUMERIC,
	bank_region VARCHAR,
	income_classification VARCHAR(2)
);