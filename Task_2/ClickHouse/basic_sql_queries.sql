-- basic_queries.sql

-- Select all data from the table
SELECT * FROM sample_data;

-- Filter by specific item
SELECT * FROM sample_data WHERE name = 'Item A';

-- Aggregate the data by name and sum the values
SELECT name, SUM(value) FROM sample_data GROUP BY name;
