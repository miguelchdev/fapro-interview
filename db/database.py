from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

sqlalchemy_database_url = "sqlite:///./fapro-desafio.db"
connect_args = {"check_same_thread": False}

if os.getenv("DOCKER_RUNNING"):
    connect_args = {}
    sqlalchemy_database_url = "postgresql://postgres:postgres@db"


engine = create_engine(sqlalchemy_database_url, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
