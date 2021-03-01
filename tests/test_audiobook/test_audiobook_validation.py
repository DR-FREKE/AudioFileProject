import unittest
from flask import request
from Server.Config.validation import Validation


class TestAudiobookValidator(unittest.TestCase):

    def test_title_not_empty(self):
        """ test that name field is not empty """

        data = {
            "audiotype": "Audiobook",
            "metadata": {
                "duration": 37477,
                "title": "another",
                "author": "Solomon",
                "narrator": "Ndiferke"
            }
        }
        result = Validation.validateAudiobook(data)
        result = result["data"]["metadata"]
        self.assertTrue(result["title"])

    def test_duration_not_empty(self):
        """ 
        test that duration field is not empty

        """
        data = {
            "audiotype": "Audiobook",
            "metadata": {
                "duration": 37477,
                "title": "another",
                "author": "Solomon",
                "narrator": "Ndiferke"
            }
        }
        result = Validation.validateAudiobook(data)
        result = result["data"]["metadata"]
        self.assertTrue(result["duration"])

    def test_duration_is_number(self):
        """ test that duration in number type """

        data = {
            "audiotype": "Audiobook",
            "metadata": {
                "duration": 37477,
                "title": "another",
                "author": "Solomon",
                "narrator": "Ndiferke"
            }
        }
        result = Validation.validateAudiobook(data)
        result = result["data"]["metadata"]
        self.assertEqual(type(result["duration"]), type(0.0))


if __name__ == "__main__":
    unittest.main()
