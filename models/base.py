# coding=utf-8

"""
	https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://tennis:tennis@seet161.mykeenetic.ru:5432/tennis')

Session = sessionmaker(bind=engine)

Base = declarative_base()