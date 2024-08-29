# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install Poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files first to leverage Docker cache
COPY pyproject.toml poetry.lock* /app/

# Install dependencies without virtualenvs
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application code
COPY . /app

# Expose port 8000
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
