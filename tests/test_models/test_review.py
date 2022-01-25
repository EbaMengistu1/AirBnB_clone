#!/usr/bin/python3
"""Test Review Class """

from models.review import Review
import datetime
import unittest


class TestReview(unittest.TestCase):
    """ Test Review Class """
    my_object = Review()
    my_class = Review.__dict__

    def test_checking_for_docstring_User(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(Review.__doc__)

    def test_subclass_instance_Review(self):
        """Test if my_object si a subclass of BaseModel"""
        self.assertTrue(isinstance(self.my_object, Review))

    def test_attribute_place_id(self):
        """ Tests attributes  of Review class"""
        self.assertEqual(hasattr(self.my_object, "place_id"), True)
        self.assertEqual(hasattr(self.my_object, "user_id"), True)
        self.assertEqual(hasattr(self.my_object, "text"), True)

    def test_attribute_type(self):
       t_format = "%Y-%m-%dT%H:%M:%S.%f"
       my_dict = self.my_object.to_dict()
       self.assertEqual(self.my_object.__class__.__name__, 'Review')
       self.assertEqual(type(my_dict['created_at']), str)
       self.assertEqual(type(my_dict['updated_at']), str)
       self.assertEqual(my_dict["created_at"],
                        self.my_object.created_at.strftime(t_format))
       self.assertEqual(my_dict["updated_at"],
                        self.my_object.updated_at.strftime(t_format))
       self.assertEqual(type(self.my_class['place_id']), str)
       self.assertEqual(type(self.my_class['user_id']), str)
       self.assertEqual(type(self.my_class['text']), str)


if __name__ == '__main__':
    unittest.main()
