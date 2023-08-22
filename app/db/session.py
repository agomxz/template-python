from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from core.config import settings


engine = create_engine("postgresql://fl0user:qQHdaz4eLYU8@ep-shrill-waterfall-75810559.us-east-2.aws.neon.tech:5432/postgres", pool_pre_ping=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
