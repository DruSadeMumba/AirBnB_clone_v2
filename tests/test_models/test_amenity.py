#!/usr/bin/python3
"""Unit Test for the BaseModel class."""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test Cases for the Amenity class."""

    def __init__(self, *args, **kwargs):
        """Initialize amenity"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
