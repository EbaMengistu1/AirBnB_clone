#!/usr/bin/python3
"""Test Place Class """

from models.place import Place
import datetime
import unittest


class TestPlace(unittest.TestCase):
    """ Test Place Class """
    my_object = Place()
    my_class = Place.__dict__

    def test_checking_for_docstring(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(Place.__doc__)

    def test_instance(self):
        """Test if my_object is a subclasses of BaseModel"""
        self.assertTrue(isinstance(self.my_object, Place))

    def test_attribute_city_id(self):
        """ Tests attributes """
        self.assertEqual(hasattr(self.my_object, "city_id"), True)
        self.assertEqual(hasattr(self.my_object, "user_id"), True)
        self.assertEqual(hasattr(self.my_object, "name"), True)
        self.assertEqual(hasattr(self.my_object, "description"), True)
        self.assertEqual(hasattr(self.my_object, "number_rooms"), True)
        self.assertEqual(hasattr(self.my_object, "number_bathrooms"), True)
        self.assertEqual(hasattr(self.my_object, "max_guest"), True)
        self.assertEqual(hasattr(self.my_object, "price_by_night"), True)
        self.assertEqual(hasattr(self.my_object, "latitude"), True)
        self.assertEqual(hasattr(self.my_object, "longitude"), True)
        self.assertEqual(hasattr(self.my_object, "amenity_ids"), True)

    def test_attribute_type(self):
       t_format = "%Y-%m-%dT%H:%M:%S.%f"
       my_dict = self.my_object.to_dict()
       self.assertEqual(self.my_object.__class__.__name__, 'Place')
       self.assertEqual(type(my_dict['created_at']), str)
       self.assertEqual(type(my_dict['updated_at']), str)
       self.assertEqual(my_dict["created_at"],
                self.my_object.created_at.strftime(t_format))
       self.assertEqual(my_dict["updated_at"],
                self.my_object.updated_at.strftime(t_format))
       self.assertEqual(type(self.my_class['city_id']), str)
       self.assertEqual(type(self.my_class['user_id']), str)
       self.assertEqual(type(self.my_class['name']), str)
       self.assertEqual(type(self.my_class['description']), str)
       self.assertEqual(type(self.my_class['number_rooms']), int)
       self.assertEqual(type(self.my_class['number_bathrooms']), int)
       self.assertEqual(type(self.my_class['max_guest']), int)
       self.assertEqual(type(self.my_class['price_by_night']), int)
       self.assertEqual(type(self.my_class['latitude']), float)
       self.assertEqual(type(self.my_class['longitude']), float)
       self.assertEqual(type(self.my_class['amenity_ids']), list)


if __name__ == '__main__':
    unittest.main()
