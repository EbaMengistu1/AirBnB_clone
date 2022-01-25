#!/usr/bin/python3
"""
Basemodel Class Tests
"""

import unittest
import os
from models.base_model import BaseModel
from datetime import datetime


class BaseModelTest(unittest.TestCase):
    """
    Tests for BaseModel Class
    """

    @classmethod
    def setUpClass(cls):
        """ Setup an instance for test"""
        cls.my_object = BaseModel()
        cls.my_object.name = "Diego"
        cls.my_object.number = 123

    @classmethod
    def teardown(cls):
        """ Delete the instance at the end of tests"""
        del cls.my_object

    def test_instance_BaseModel(self):
        """Test if my_object is instance of BaseModel"""
        self.assertTrue(isinstance(self.my_object, BaseModel))

    def test_str(self):
        """Test if __str__ method show the right output"""
        string = "[BaseModel] ({}) {}".format(self.my_object.id,
                                              self.my_object.__dict__)
        self.assertEqual(string, str(self.my_object))

    def test_BaseModel(self):
        """Checks if BaseModel works"""
        self.assertIs(type(self.my_object.id), str)
        self.assertIs(type(self.my_object.created_at), datetime)
        self.assertIs(type(self.my_object.updated_at), datetime)
        self.assertNotEqual(self.my_object.created_at,
                            self.my_object.updated_at)
        self.assertFalse(self.my_object.updated_at == datetime.utcnow())

    def test_save_BaseModel(self):
        """Test if updated changes"""
        self.my_object.save()
        self.assertIsInstance(self.my_object.to_dict()['created_at'], str)
        self.assertIsInstance(self.my_object.to_dict()['updated_at'], str)

    def test_from_dict_to_BaseModel(self):
        """Test if we can create an instance from a dictionary"""
        my_object_json = self.my_object.to_dict()
        new_object = BaseModel(**my_object_json)
        self.assertTrue(isinstance(new_object, BaseModel))
        self.assertEqual(new_object.name, "Diego")
        self.assertEqual(new_object.number, 123)
        self.assertEqual(new_object.id, self.my_object.id)
        self.assertEqual(new_object.created_at, self.my_object.created_at)
        self.assertEqual(new_object.updated_at, self.my_object.updated_at)
        self.assertNotEqual(new_object, self.my_object)

    def test_to_dict_BaseModel(self):
        """Checks if the convertion to dictionary works"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        my_dict = self.my_object.to_dict()
        self.assertEqual(self.my_object.__class__.__name__, 'BaseModel')
        self.assertEqual(type(my_dict['created_at']), str)
        self.assertEqual(type(my_dict['updated_at']), str)
        self.assertEqual(my_dict["created_at"],
                         self.my_object.created_at.strftime(t_format))
        self.assertEqual(my_dict["updated_at"],
                         self.my_object.updated_at.strftime(t_format))

if __name__ == '__main__':
    unittest.main()
