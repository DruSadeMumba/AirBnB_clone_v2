#!/usr/bin/python3
"""manage db storage"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


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
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dic[key] = obj
        return dic

    def new(self, obj):
        """create new obj in db"""
        self.__session.add(obj)

    def save(self):
        """save obj in db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from db"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload db"""
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        sessions = scoped_session(sess)
        self.__session = sessions

    def close(self):
        """close session"""
        self.__session.close()
