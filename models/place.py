#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base
from models.review import Review

metadata = Base.metadata
place_amenity = Table("place_amenity", metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60), ForeignKey(
                          "amenities.id"), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade="all, delete, delete-orphan",
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            return [review for review in models.storage.all(Review).values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            return self.amenity_ids

        @amenities.setter
        def amenities(self, amen):
            if isinstance(amen, Amenity):
                self.amenity_ids.append(amen.id)
