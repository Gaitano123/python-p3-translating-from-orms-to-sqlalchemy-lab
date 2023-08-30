from models import Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def create_table(base, engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the table using the base's metadata
    base.metadata.create_all(engine)
    pass
if __name__ == '__main__':
    SQLITE_URL = 'sqlite:///dogs.db'
    engine = create_engine(SQLITE_URL)
    Base = declarative_base()

    create_table(Base, engine)
    
    
def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return list([dog for dog in session.query(Dog)])

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()
    pass

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    pass

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    pass