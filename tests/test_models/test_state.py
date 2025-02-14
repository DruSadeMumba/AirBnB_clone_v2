#!/usr/bin/python3
"""Unit Test for the State."""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Test Cases for the State class."""

    def __init__(self, *args, **kwargs):
        """Initialize state"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
