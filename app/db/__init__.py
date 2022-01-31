from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

load_dotenv()

# connect to database using env variable
# manage overall connection to the database
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# generate temporary connections for performing crud operations
Session = sessionmaker(bind=engine)
# helps us map the models to real MySQL tables
Base = declarative_base()

# initiates the connection between Base and the database
def init_db(app):
    Base.metadata.create_all(engine)
    # close the database connection
    app.teardown_appcontext(close_db)


def get_db():
    # this function saves the current connection on the g object if it's not already there
    # then it returns the connection from the g object instead of creating a new Session instance each time
    if 'db' not in g:
        # store db connection in app context
        g.db = Session()
    
    return g.db

# put 'python3 app/db/__init__.py' into terminal to test db connection
# if there are no errors the connection was successful

def close_db(e=None):
    # find and remove db from the g object
    db = g.pop('db', None)
    
    # if db exists then end the connection
    if db is not None:
        db.close()