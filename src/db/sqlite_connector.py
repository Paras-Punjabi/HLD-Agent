from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.env import config
from db.schema import *

engine = create_engine(config.DB_URL, echo=True)

session = sessionmaker(bind=engine)()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Tables Populated")



