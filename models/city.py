##!/usr/bin/python3
"""This is the city class"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
        places: relationship between a city and places
    """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    places = relationship(
        'Place', backref='cities', cascade='all, delete-orphan'
    )
