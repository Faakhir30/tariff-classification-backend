# Tariff Classification Project

This project is a FastAPI-based application for tariff classification, utilizing Poetry for package management. The local development environment leverages Docker to run a PostgreSQL database, ensuring a consistent and isolated setup across different development environments.
Features

- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- Poetry: Python dependency management and packaging made easy.
- PostgreSQL: A powerful, open-source object-relational database system used for storing application data.
- Docker: Containerized PostgreSQL for isolated and consistent database management.


Project Structure


```plaintext
├── app/
│   ├── controllers/
│   ├── models/
│   ├── routers/
│   ├── session/
│   ├── types/
│   └── utils/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

**Getting Started**
Prerequisites

- Docker
- Poetry

**Installation**

- Clone the repository:

```bash
git clone https://github.com/yourusername/tariff-classification-backend.git
cd tariff-classification-backend
```

**Install Python dependencies:**

```bash
poetry install
```

**Set up the environment variables:**

Create a .env file in the root directory to configure your environment variables. Here is an example:

```plaintext
    DATABASE_URL=postgresql://postgres:password@localhost:5432/mydatabase
```

**Running the Application**

1. Start PostgreSQL with Docker:

    Use Docker Compose to set up and run the PostgreSQL container.

```bash
docker-compose up -d
```

2. Run the FastAPI application:

    After the database is up and running, you can start your FastAPI application:

```bash
    poetry run uvicorn app.main:api_app --reload
```

Your FastAPI application will now be running on http://localhost:8000.

**Managing the PostgreSQL Container**

Start the container:

```bash
docker-compose start
```

Stop the container:

```bash
docker-compose stop
```

Remove the container:

```bash
    docker-compose down
```

**Database Backup and Restore**

- Backup your PostgreSQL database:

```bash
docker exec -t postgres-db pg_dump -U postgres mydatabase > backup.sql
```

- Restore your PostgreSQL database:

```bash
    docker exec -i postgres-db psql -U postgres -d mydatabase < backup.sql
```

**Testing**

You can run tests using pytest. Make sure to have your environment set up and the database running:

```bash
poetry run pytest
```

**Contributing**

_Contributions are welcome! Please open an issue or submit a pull request._

**License**

_This project is licensed under the MIT License. See the LICENSE file for more details._

**Acknowledgements**

- Thanks to the open-source community for providing the tools and libraries that make this project possible.