from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# connect to database using env variable
# manage overall connection to the database
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# generate temporary connections for performing crud operations
Session = sessionmaker(bind=engine)
# helps us map the models to real MySQL tables
Base = declarative_base()

# put 'python3 app/db/__init__.py' into terminal to test db connection
# if there are no errors the connection was successful