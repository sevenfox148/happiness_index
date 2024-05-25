CREATE SCHEMA warehouse;

CREATE TABLE warehouse.dim_region(
    id SERIAL PRIMARY KEY,
    region VARCHAR(30)
);

CREATE TABLE warehouse.dim_bank_region(
     id SERIAL PRIMARY KEY,
     bank_region VARCHAR(50)
);

CREATE TABLE warehouse.dim_country(
    iso2 CHAR(2) PRIMARY KEY,
    iso3 CHAR(3),
    country VARCHAR(30),
    region INTEGER REFERENCES warehouse.dim_region(id),
    bank_region INTEGER REFERENCES warehouse.dim_bank_region(id)
);

CREATE TABLE warehouse.dim_date(
    year INT PRIMARY KEY
);

CREATE TABLE warehouse.dim_income_class(
    income_class VARCHAR(2) PRIMARY KEY
);

CREATE TABLE warehouse.dim_freedom_status(
    status VARCHAR(2) PRIMARY KEY
);

CREATE TABLE warehouse.fact_happiness(
    id SERIAL PRIMARY KEY,
    country CHAR(2) REFERENCES warehouse.dim_country(iso2),
    year INT REFERENCES warehouse.dim_date(year),
    index NUMERIC,
    gdp_per_capita NUMERIC,
    soc_support NUMERIC,
    life_expectancy NUMERIC,
    freedom NUMERIC,
    generosity NUMERIC,
    corruption NUMERIC,
    positive_affect NUMERIC,
    negative_affect NUMERIC,
    government NUMERIC
);

CREATE TABLE warehouse.fact_pol_freedom(
    id SERIAL PRIMARY KEY,
    country CHAR(2) REFERENCES warehouse.dim_country(iso2),
    year INT REFERENCES warehouse.dim_date(year),
    status VARCHAR(2) REFERENCES warehouse.dim_freedom_status(status),
    total INTEGER,
    electoral_process INTEGER,
    pluralism INTEGER,
    gov_functioning INTEGER,
    pol_rights INTEGER,
    belief_freedom INTEGER,
    organizations INTEGER,
    law INTEGER,
    individual INTEGER,
    civil_liberties INTEGER
);

CREATE TABLE warehouse.fact_econ_freedom(
    id SERIAL PRIMARY KEY,
    country CHAR(2) REFERENCES warehouse.dim_country(iso2),
    year INT REFERENCES warehouse.dim_date(year),
    income_class VARCHAR(2) REFERENCES warehouse.dim_income_class(income_class),
    index NUMERIC,
    government_index NUMERIC,
    legal_index NUMERIC,
    sound_money NUMERIC,
    international_trade NUMERIC,
    regulations NUMERIC
);