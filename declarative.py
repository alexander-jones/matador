import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, Integer, SmallInteger, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from config import Config

Base = declarative_base()
 
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    salt = Column(String(250), nullable=False)
    rank = Column(SmallInteger, default=0)
    points = Column(Integer, default=0)
    description = Column(String(250))

class League(Base):
    __tablename__ = 'league'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    owner = Column(Integer, ForeignKey('user.id'), nullable=False)
    principle = Column(Float, nullable=False)
    goal = Column(Float)
    term_start = Column(DateTime, nullable=False)
    term_end = Column(DateTime)
    last_updated = Column(DateTime, nullable=False)
    completed = Column(Boolean, default=True)
    min_users = Column(SmallInteger)
    max_users = Column(SmallInteger)
    min_stocks = Column(SmallInteger)
    max_stocks = Column(SmallInteger)

class Placement(Base):
    __tablename__ = 'placement'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('user.id'), nullable=False)
    league = Column(Integer, ForeignKey('league.id'), nullable=False)
    rank = Column(SmallInteger)
    value = Column(Float, nullable=False)

class Investment(Base):
    __tablename__ = 'investment'
    id = Column(Integer, primary_key=True)
    placement = Column(Integer, ForeignKey('placement.id'), nullable=False)
    symbol = Column(String(250), nullable=False)
    volume = Column(Integer, nullable=False)
    term_start = Column(DateTime, nullable=False)
    term_end = Column(DateTime, nullable=False)
    start_price = Column(Float, nullable=False)
    last_price = Column(Float, nullable=False)
    last_price_time = Column(DateTime, nullable=False)

if __name__ == "__main__":
	engine = create_engine(Config.TEST_ENGINE)
	Base.metadata.create_all(engine)