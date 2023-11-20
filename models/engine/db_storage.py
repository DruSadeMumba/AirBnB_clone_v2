#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models.base_model import Base, BaseModel


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate db storage"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        engine = create_engine(
            f'mysql+mysqldb://{user}:{passwd}@{host}/{db}', pool_pre_ping=True)

        self.__engine = engine
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """get all obj"""
        dic = {}
        if cls:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = f"{type(obj).__name__}.{obj.id}"
                dic[key] = obj
        for all_cls in BaseModel.__subclasses__():
            objects = self.__session.query(all_cls).all()
            for obj in objects:
                key = f"{type(obj).__name__}.{obj.id}"
                dic[key] = obj
        return dic

    def new(self, obj):
        """create new obj in db"""
        with self.__session.begin():
            self.__session.add(obj)

    def save(self):
        """save obj in db"""
        with self.__session.begin():
            self.__session.commit()

    def delete(self, obj=None):
        """delete obj from db"""
        if obj:
            with self.__session.begin():
                self.__session.delete(obj)

    def reload(self):
        """reload db"""
        Base.metadata.create_all(self.__engine)
        self.__session = Session(self.__engine)
