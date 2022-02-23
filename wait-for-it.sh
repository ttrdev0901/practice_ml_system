#!/bin/sh

set -e
    
until PGPASSWORD=$DBPASSWORD psql -h $DBHOST -U $DBUSER --dbname $DBNAME -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
  
>&2 echo "Postgres is up - executing command"
exec uvicorn main