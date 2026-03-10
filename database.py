from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# บน Azure เราจะดึง Connection String จาก Environment Variable
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db") 

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class URLModel(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String, unique=True, index=True)
    full_url = Column(String)

# สร้าง Table
Base.metadata.create_all(bind=engine)