import unittest
import requests


class TestSongResponse(unittest.TestCase):

    def test_song_can_insert(self):
        """ test that song can be inserted into db """
        data = {"audiotype": "Song", "metadata": {
            "duration": 37477, "name": "small world"}}
        response = requests.post(
            "http://localhost:9001/api/create-audio", data=data)

        success = response.json()

        print(success)

        self.assertEqual(success["success"], True)

    def test_song_can_read(self):
        """ test that song can be read from DB """
        response = requests.get("http://localhost:9001/api/get-audio/Song")

        self.assertEqual(response.status_code, 200)

    def test_song_can_delete(self):
        """ test that song can be deleted from DB"""
        response = requests.delete(
            "http://localhost:9001/api/delete-audio/Song/8")

        self.assertEqual(response.status_code, 200)

    def test_song_can_update(self):
        """ test that song can be updated in DB"""


if __name__ == "__main__":
    unittest.main()