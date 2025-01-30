#!/bin/bash

# Upgrade the Superset database
superset db upgrade

# Create an admin user for Superset (change username, email, and password as needed)
superset fab create-admin \
  --username admin \
  --firstname Admin \
  --lastname User \
  --email admin@example.com \
  --password admin

# Initialize Superset
superset init
