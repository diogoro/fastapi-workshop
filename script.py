from typing import Optional
from sqlmodel import SQLModel, Field, create_engine, Session

engine = create_engine(url="sqlite:///users.db", echo=True)

class User(SQLModel, table=True):
    id:Optional[int] = Field(None, primary_key=True)
    username: str
    password:str

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.create_all(engine)