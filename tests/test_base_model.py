#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    def setup(self):
        """reload storage before each test"""
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """saves storage after each test"""
        self.storage.save()

    def test_attributes(self):
        """Test if attributes are initialized correctly"""
        base_model = BaseModel()

        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)
        self.assertEqual(base_model.created_at, base_model.updated_at)

    def test_save_method(self):
        """Test the save method"""
        base_model = BaseModel()
        base_model.save()
        self.assertNotEqual(base_model.created_at, base_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        base_model = BaseModel()
        obj_dict = base_model.to_dict()

        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['created_at'], base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], base_model.updated_at.isoformat())

    def test_str_method(self):
        """Test the __str__ method"""
        base_model = BaseModel()

        expected_str = "[BaseModel] ({}) {}".format(base_model.id, base_model.__dict__)
        self.assertEqual(str(base_model), expected_str)

    def test_init_method_with_kwargs(self):
        """ Test __init__ method with kwargs"""
        data = {
            'id': '123',
            'created_at': '2024-05-14T12:30:00.000000',
            'updated_at': '2024-05-14T12:30:00.000000',
        }
        base_model = BaseModel(**data)

        self.assertEqual(base_model.id, '123')
        self.assertEqual(base_model.created_at, datetime(2024, 5, 14, 12, 30))
        self.assertEqual(base_model.updated_at, datetime(2024, 5, 14, 12, 30))

    def test_new_method(self):
        """test the new method of FileStorage"""
        base_model = BaseModel()
        all_objects_before = self.storage.all()
        self.storage.new(base_model)
        all_objects_after = self.storage.all()
        self.assertIn('BaseModel.' + base_model.id, all_objects_after)
        self.assertEqual(all_objects_before, all_objects_after)

if __name__ == '__main__':
    unittest.main()
