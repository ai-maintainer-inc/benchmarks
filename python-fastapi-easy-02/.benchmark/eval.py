import unittest
import requests
from datetime import datetime

BASE_URL = "http://localhost:8000/items"  # Replace with your API base URL


class TestApi(unittest.TestCase):
    def test_1_post(self):
        item = {"name": "Test Item"}
        response = requests.post(BASE_URL, json=item)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())
        self.assertIn("created_at", response.json())
        self.assertIn("updated_at", response.json())

    def test_2_get_all(self):
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_3_get_single(self):
        # Create an item to test
        item = {"name": "Test Item for Get Single"}
        response = requests.post(BASE_URL, json=item)
        item_id = response.json()["id"]

        # Now, get it by ID
        response = requests.get(f"{BASE_URL}/{item_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], item_id)
        self.assertEqual(response.json()["name"], item["name"])

    def test_4_put(self):
        # Create an item to test
        item = {"name": "Test Item for Update"}
        response = requests.post(BASE_URL, json=item)
        item_id = response.json()["id"]

        # Update the item
        updated_item = {"name": "Updated Item"}
        response = requests.put(f"{BASE_URL}/{item_id}", json=updated_item)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], updated_item["name"])

    def test_5_delete(self):
        # Create an item to delete
        item = {"name": "Test Item for Delete"}
        response = requests.post(BASE_URL, json=item)
        item_id = response.json()["id"]

        # Delete the item
        response = requests.delete(f"{BASE_URL}/{item_id}")
        self.assertEqual(response.status_code, 200)

        # Try to get the deleted item
        response = requests.get(f"{BASE_URL}/{item_id}")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main(exit=False)

    # If no tests fail, exit with 0, otherwise 1
    if (
        len(unittest.TestResult().failures) == 0
        and len(unittest.TestResult().errors) == 0
    ):
        exit(0)
    else:
        exit(1)
