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
        num = str(9)
        response = requests.delete(
            "http://localhost:9001/api/delete-audio/Song/"+num)

        self.assertEqual(response.status_code, 200)

    def test_song_can_update(self):
        """ test that song can be updated in DB"""

        data = {"audiotype": "Song", "metadata": {
            "duration": 37477, "name": "smalls world"}}

        response = requests.put(
            "http://localhost:9001/api/update-audio/Song/9", data=data)

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
