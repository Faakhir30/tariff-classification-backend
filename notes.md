Access PostgreSQL
From Your Local Machine (e.g., with psql CLI or a GUI like pgAdmin):

You can connect to PostgreSQL using the following details:

- Host: localhost
- Port: 5432
- Username: postgres (or whatever you set in POSTGRES_USER)
- Password: password (or whatever you set in POSTGRES_PASSWORD)
- Database: mydatabase (or whatever you set in POSTGRES_DB)


To connect via the command line using psql:
```bash
psql -h localhost -p 5432 -U postgres -W
```

This will prompt for the password (password as set in the compose file).


Alternatively, you can use a PostgreSQL client like pgAdmin, DBeaver, or TablePlus to manage the database using the same connection details.
5. Persist Data Between Restarts

The data you store in the database will persist even if you stop and remove the container, thanks to the volumes configuration in your docker-compose.yml file:

yaml
```
volumes:
  postgres-data:
```

This creates a named volume (postgres-data) that will store your PostgreSQL data outside of the container. This way, your data is safe even if the container is destroyed.
6. Manage Your PostgreSQL Container

    Start the container:
```bash
docker-compose start
```
Stop the container:
```bash
docker-compose stop
```

Remove the container (useful if you want to start fresh):
```bash
docker-compose down
```

View container logs:
```bash
docker-compose logs -f
```



Backup and Restore PostgreSQL Data

To manually backup or restore your PostgreSQL data, you can run pg_dump and psql commands inside the Docker container:

Backup:
```bash
docker exec -t postgres-db pg_dump -U postgres mydatabase > backup.sql
```

Restore:
```bash
docker exec -i postgres-db psql -U postgres -d mydatabase < backup.sql
```

Example docker-compose.yml Breakdown

    image: We specify postgres:13, which tells Docker to pull the PostgreSQL 13 image from Docker Hub. You can specify any other version here as needed.
    environment: These environment variables configure the PostgreSQL container. They include the username, password, and default database to create when the container first starts.
    ports: We map port 5432 from the container to port 5432 on the host machine, so we can connect to PostgreSQL via localhost:5432.
    volumes: We specify a volume to persist the database data outside the container, ensuring that data isn't lost if the container is stopped or removed.

