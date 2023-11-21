#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") == "db",
    "Test is not relevant for BaseModel"
)
class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""
    def __init__(self, *args, **kwargs):
        """initialize basemodel"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up test methods."""
        pass

    def tearDown(self):
        """Tear down test methods."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """Test default"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test kwargs int"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test save"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test str"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                                                       i.__dict__))

    def test_todict(self):
        """Test to dict"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test kwargs none"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Test kwargs one"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """Test id"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test created at"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test updated at"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
