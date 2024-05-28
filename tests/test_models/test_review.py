import unittest
from models.place import Place
from models.base_model import BaseModel
import models

def TestReview(unittest.TestCase):
    """Testcases for Review"""

    def setUp(self):
        """Reload storage before each test"""
        models.storage.reload()
        models.storage.all().clear()

    def tearDown(self):
        """Clear storage after each test"""
        models.storage.save()
        models.storage.all().clear()

    def test_review_attributes(self):
        """
        Test if review attributes are correctly set and are strings.
        """
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertEqual(review.place_id, "")
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertEqual(review.user_id, "")
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
