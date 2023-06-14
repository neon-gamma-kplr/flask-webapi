from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin


url = "postgres://nxsoxgro:vpvuRLZZoKafSSjF9mfm0z5Ehj0x1Hcg@horton.db.elephantsql.com/nxsoxgro"

# an Engine, which the Session will use for connection
# resources, typically in module scope
engine = create_engine(url)

# a sessionmaker(), also in the same scope as the engine
Session = sessionmaker(engine)

Base = declarative_base()

# Base.query = db_session.query_property()

# # we can now construct a Session() without needing to pass the
# # engine each time
# with Session() as session:
#     session.add(some_object)
#     session.add(some_other_object)
#     session.commit()
# # closes the session



class User(Base, UserMixin):

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(20), nullable=False)
    name = Column(String(100), nullable=False)

    def __init__(self, id, email, password, name):
        self.id = id,
        self.email = email,
        self.password = password,
        self.name = name

    def __repr__(self):
        pass


# users = Table('users', metadata,
# ...               Column('id', Integer, primary_key=True)
# ...               Column('login', String(32))
# ...              )

class IncomeExpenses(Base):

    id = Column(Integer, primary_key=True)
    type = Column(String(30), default='income')
    value = Column(Integer)
    date = Column(DateTime)

    def __init__(self, id, type):
        self.id = id,
        self.type = type

    def __repr__(self):
        pass

