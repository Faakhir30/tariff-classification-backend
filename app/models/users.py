from sqlmodel import SQLModel, Field, create_engine, Session, select


# Define the User model
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    full_name: str
    disabled: Optional[bool] = False