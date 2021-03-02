import unittest
import requests


class TestPodcastResponse(unittest.TestCase):

    def test_podcast_can_insert(self):
        """ test that podcast can be inserted into db """

        data = {
            "audiotype": "Podcast",
            "metadata": {
                "duration": 37477,
                "name": "small world",
                "host": "Solomon",
                "participants": ["lee", "Daniel", "lukeng"]
            }
        }
        response = requests.post(
            "http://localhost:9001/api/create-audio", json=data)

        success = response.json()

        self.assertEqual(success["success"], True)

    def test_podcast_can_read(self):
        """ test that podcast can be read from DB """

        response = requests.get("http://localhost:9001/api/get-audio/Podcast")

        self.assertEqual(response.status_code, 200)

    def test_podcast_can_delete(self):
        """ test that podcast can be deleted from DB"""

        num = str(9)
        response = requests.delete(
            "http://localhost:9001/api/delete-audio/Podcast/"+num)

        self.assertEqual(response.status_code, 200)

    def test_podcast_can_update(self):
        """ test that podcast can be updated in DB"""

        data = {
            "audiotype": "Podcast",
            "metadata": {
                "duration": 37477,
                "name": "small world",
                "host": "Solomon",
                "participants": ["lee", "Daniel", "lukeng"]
            }
        }

        num = str(9)

        response = requests.put(
            "http://localhost:9001/api/update-audio/Podcast/"+num, json=data)

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
