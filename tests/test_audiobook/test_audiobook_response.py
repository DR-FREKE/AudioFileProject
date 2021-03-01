import unittest
import requests


class TestAudiobookResponse(unittest.TestCase):

    def test_audiobook_can_insert(self):
        """ test that audiobook can be inserted into db """

        data = {
            "audiotype": "Audiobook",
            "metadata": {
                "duration": 37477,
                "title": "another",
                "author": "Solomon",
                "narrator": "Ndiferke"
            }
        }
        response = requests.post(
            "http://localhost:9001/api/create-audio", data=data)

        success = response.json()
        self.assertEqual(success["success"], True)

    def test_audiobook_can_read(self):
        """ test that audiobook can be read from DB """

        response = requests.get(
            "http://localhost:9001/api/get-audio/Audiobook")

        self.assertEqual(response.status_code, 200)

    def test_audiobook_can_delete(self):
        """ test that audiobook can be deleted from DB"""
        num = str(4)
        response = requests.delete(
            "http://localhost:9001/api/delete-audio/Audiobook/"+num)

        self.assertEqual(response.status_code, 200)

    def test_audiobook_can_update(self):
        """ test that audiobook can be updated in DB"""

        data = {
            "audiotype": "Audiobook",
            "metadata": {
                "duration": 37477,
                "title": "another",
                "author": "Solomon",
                "narrator": "Ndiferke"
            }
        }

        num = str(3)

        response = requests.put(
            "http://localhost:9001/api/update-audio/Audiobook/"+num, data=data)

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
