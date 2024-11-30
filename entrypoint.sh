#!/bin/sh
# Wait for the database to be ready
until pg_isready -h webapi -p 5432; do
  echo "Waiting for database to be ready..."
  sleep 2
done

# Run Alembic migrations
alembic upgrade head

# Start the main application
exec python3 main.py
