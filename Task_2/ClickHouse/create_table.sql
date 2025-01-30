-- create_table.sql
CREATE TABLE sample_data (
    date Date,
    name String,
    value Int32
) ENGINE = MergeTree()
ORDER BY date;
