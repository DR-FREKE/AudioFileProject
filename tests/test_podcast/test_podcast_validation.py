import unittest
from flask import request
from Server.Config.validation import Validation


class TestPodcastValidator(unittest.TestCase):

    def test_name_not_empty(self):
        """ test that name field is not empty """

        data = {
            "audiotype": "Podcast",
            "metadata":
            {
                "duration": 37477,
                "name": "small world",
                "host": "Solomon",
                "participants": ["lee", "Daniel", "lukeng"]
            }
        }
        result = Validation.validatePodcast(data)
        result = result["data"]["metadata"]
        self.assertTrue(result["name"])

    def test_duration_not_empty(self):
        """
        test that duration field is not empty

        """
        data = {
            "audiotype": "Podcast",
            "metadata":
            {
                "duration": 37477,
                "name": "small world",
                "host": "Solomon",
                "participants": ["lee", "Daniel", "lukeng"]
            }
        }
        result = Validation.validatePodcast(data)
        result = result["data"]["metadata"]
        self.assertTrue(result["duration"])

    def test_host_not_empty(self):
        """
        test that host field is not empty

        """
        data = {
            "audiotype": "Podcast",
            "metadata":
            {
                "duration": 37477,
                "name": "small world",
                "host": "Solomon",
                "participants": ["lee", "Daniel", "lukeng"]
            }
        }
        result = Validation.validatePodcast(data)
        result = result["data"]["metadata"]
        self.assertTrue(result["host"])

    def test_duration_is_number(self):
        """ test that duration in number type """

        data = {
            "audiotype": "Podcast",
            "metadata":
            {
                "duration": 37477,
                "name": "small world",
                "host": "Solomon",
                "participants": ["lee", "Daniel", "lukeng"]
            }
        }
        result = Validation.validatePodcast(data)
        result = result["data"]["metadata"]
        self.assertEqual(type(result["duration"]), type(0.0))


if __name__ == "__main__":
    unittest.main()
