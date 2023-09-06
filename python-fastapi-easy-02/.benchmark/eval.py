import unittest
import requests
from datetime import datetime

BASE_URL = "http://localhost:8000"  # Replace with your API base URL
ITEMS_URL = BASE_URL + "/items"


class TestApi(unittest.TestCase):
    def test_ping(self):
        response = requests.get(BASE_URL + "/ping")
        self.assertEqual(response.status_code, 200)

    def test_1_post(self):
        item = {"name": "Test Item"}
        response = requests.post(ITEMS_URL, json=item)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())
        self.assertIn("created_at", response.json())
        self.assertIn("updated_at", response.json())

    def test_2_get_all(self):
        response = requests.get(ITEMS_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_3_get_single(self):
        # Create an item to test
        item = {"name": "Test Item for Get Single"}
        response = requests.post(ITEMS_URL, json=item)
        item_id = response.json()["id"]

        # Now, get it by ID
        response = requests.get(f"{ITEMS_URL}/{item_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], item_id)
        self.assertEqual(response.json()["name"], item["name"])

    def test_4_put(self):
        # Create an item to test
        item = {"name": "Test Item for Update"}
        response = requests.post(ITEMS_URL, json=item)
        item_id = response.json()["id"]

        # Update the item
        updated_item = {"name": "Updated Item"}
        response = requests.put(f"{ITEMS_URL}/{item_id}", json=updated_item)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], updated_item["name"])

    def test_5_delete(self):
        # Create an item to delete
        item = {"name": "Test Item for Delete"}
        response = requests.post(ITEMS_URL, json=item)
        item_id = response.json()["id"]

        # Delete the item
        response = requests.delete(f"{ITEMS_URL}/{item_id}")
        self.assertEqual(response.status_code, 200)

        # Try to get the deleted item
        response = requests.get(f"{ITEMS_URL}/{item_id}")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApi)
    result = unittest.TextTestRunner().run(suite)

    # Exit based on the test results
    if result.wasSuccessful():
        exit(0)
    else:
        exit(1)
