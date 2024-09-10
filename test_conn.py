from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/mydatabase"
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        result = connection.execute("SELECT 1")
        print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
