import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    mail = Column(String(50))
    password = Column(String(50))
    subscription_date = Column(String(50))
    first_name = Column(String(20))
    last_name = Column(String(20))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    height = Column(String(50))
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    user_id = Column(Integer, ForeignKey('user.id'))


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    rotation_period = Column(String(20))
    climate = Column(String(20))
    terrain = Column(String(20))
    populations = Column(String(20))
    user_id = Column(Integer, ForeignKey('user.id'))

class FavoriteCharacters(Base): 
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    create_at = Column(String(50))

class FavoritesPlanets(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    planest_id = Column(Integer, ForeignKey('planets.id'))
    create_at = Column(String(50))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
