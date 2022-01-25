#!/usr/bin/python3
"""Test of City Class """

from models.city import City
import datetime
import unittest


class TestCity(unittest.TestCase):
    """ Test City Class """
    my_object = City()
    my_class = City.__dict__

    def test_checking_for_docstring_User(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(City.__doc__)

    def test_subclass_instance_User(self):
        """Test if my_object 1 is a subclass of BaseModel"""
        self.assertTrue(isinstance(self.my_object, City))

    def test_attribute(self):
        """ Tests attributes"""
        self.assertEqual(hasattr(self.my_object, "state_id"), True)
        self.assertEqual(hasattr(self.my_object, "name"), True)

    def test_attribute_type(self):
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        my_dict = self.my_object.to_dict()
        self.assertEqual(self.my_object.__class__.__name__, 'City')
        self.assertEqual(type(my_dict['created_at']), str)
        self.assertEqual(type(my_dict['updated_at']), str)
        self.assertEqual(my_dict["created_at"],
                         self.my_object.created_at.strftime(t_format))
        self.assertEqual(my_dict["updated_at"],
                         self.my_object.updated_at.strftime(t_format))
        self.assertEqual(type(self.my_class['state_id']), str)
        self.assertEqual(type(self.my_class['name']), str)
        

if __name__ == '__main__':
    unittest.main()
