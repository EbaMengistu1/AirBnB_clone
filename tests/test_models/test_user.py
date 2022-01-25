#!/usr/bin/python3
"""Test of User Class """

from models.base_model import BaseModel
from models.user import User
import datetime
import unittest


class TestUser(unittest.TestCase):
    """ Test User Class """
    my_object = User()
    my_object.name = "Diego"

    def test_checking_for_docstring_User(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(User.__doc__)

    def test_subclass_instance_User(self):
        """Test if my_object is a subclasses of BaseModel"""
        self.assertTrue(isinstance(self.my_object, User))

    def test_attribute_city(self):
        """Test attributes of User class"""
        self.assertTrue(hasattr(self.my_object, 'email'))
        self.assertTrue(hasattr(self.my_object, 'password'))
        self.assertTrue(hasattr(self.my_object, 'first_name'))
        self.assertTrue(hasattr(self.my_object, 'last_name'))

    def test_hasattr(self):
        """ attributes inheritated from BaseModel"""
        self.assertTrue(hasattr(self.my_object, 'name'))
        self.assertTrue(hasattr(self.my_object, 'id'))
        self.assertTrue(hasattr(self.my_object, 'created_at'))
        self.assertTrue(hasattr(self.my_object, 'updated_at'))

    def test_attributes_types(self):
        """Tests attributes types"""
        self.assertEqual(type(self.my_object.email), str)
        self.assertEqual(type(self.my_object.last_name), str)
        self.assertEqual(type(self.my_object.first_name), str)
        self.assertEqual(type(self.my_object.password), str)
        self.assertIsInstance(self.my_object.created_at, datetime.datetime)
        self.assertIsInstance(self.my_object.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
