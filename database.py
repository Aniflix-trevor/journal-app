from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Replace this with your actual database URL
DATABASE_URL = "sqlite:///./journal.db"
# Example for PostgreSQL: "postgresql://user:password@localhost/dbname"

# Create the SQLAlchemy engine
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

# Create a configured "SessionLocal" class
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

# Base class for all models
Base = declarative_base()
