#!/bin/bash

# Replace with your ClickHouse details
CLICKHOUSE_URI="clickhouse+native://default:@localhost:9000/default"

# Add ClickHouse as a database source in Superset
superset database add --database clickhouse --uri "$CLICKHOUSE_URI"

# You can also confirm the connection with the following command:
superset db upgrade
