import unittest
from models.place import Place
from models.base_model import BaseModel
import models

def TestPlace(unittest.TestCase):
    """Testcases for Place"""

    def setUp(self):
        """Reload storage before each test"""
        models.storage.reload()
        models.storage.all().clear()

    def tearDown(self):
        """Clear storage after each test"""
        models.storage.save()
        models.storage.all().clear()

    def test_place_attributes(self):
        """
        Test if place attributes are correctly set and are strings.
        """
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertEqual(place.city_id, "")
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertEqual(place.user_id, "")
        self.assertTrue(hasattr(place, 'name'))
        self.assertEqual(place.name, "")
        self.assertTrue(hasattr(place, 'description'))
        self.assertEqual(place.description, "")
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertEqual(place.number_rooms, int)
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertEqual(place.number_bathrooms, int)
        self.assetTrue(hasattr(place, 'max_guest'))
        self.assertEqual(place.max_guest, int)
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertEqual(place.price_by_night, int)
        self.assertTrues(hasattr(place, 'latitude'))
        self.assertEqual(place.latitude, float)
        self.assertTrue(hasattr(place, 'longitude'))
        self.asserEqual(place.longitude, float)
        self.assertTrue(hasattr(place, 'amenity_ids'))
        self.assertEqual(place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
