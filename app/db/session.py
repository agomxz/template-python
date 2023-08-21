from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#from core.config import settings

##BASE DE DATOS
user = 'aldair.rgomez'
password = 'b62oATEkqgPM'
host = 'ep-super-mud-353804.us-east-2.aws.neon.tech'
port = '5432'
dbname = 'neondb'





#engine = create_engine("postgresql://aldair.rgomez:b62oATEkqgPM@ep-super-mud-353804.us-east-2.aws.neon.tech/neondb", pool_pre_ping=True)

engine = create_engine("postgresql://aldairrgomez:v2_42ZeL_RH3GzYU5afGC8cX9jpMyMdL@db.bit.io:5432/aldairrgomez/users", pool_pre_ping=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
