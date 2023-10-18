from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an SQLite database

# Create a base class for declarative class definitions
Base = declarative_base()

# Define a sample table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    salt = Column(String)

    def __init__(self, username, email, password, salt):
        self.username = username
        self.email = email
        self.password = password
        self.salt = salt
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}', '{self.salt}')"

# Create the table
engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base.metadata.create_all(bind=engine)

#test

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()


#person = User(username="jirka", email="pepazdepa", password="pepazdepa", salt="")
#session.add(person)
#session.commit()
#session.close()
