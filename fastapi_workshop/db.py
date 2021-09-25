from typing import Optional
from sqlmodel import SQLModel, create_engine, Session


from .config import settings

engine = create_engine(
    url=settings.db.url,
    echo=settings.db.echo,
    connect_args=settings.db.connect_args
)


def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.create_all(engine)