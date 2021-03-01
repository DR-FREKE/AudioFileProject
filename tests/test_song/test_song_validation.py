import unittest
from flask import request
from Server.Config.validation import Validation


class TestSongValidator(unittest.TestCase):

    def test_name_not_empty(self):
        """ test that name field is not empty """

        data = {
            "audiotype": "Song",
            "metadata":
            {
                "duration": 37477,
                "name": "My Book",
            }
        }
        result = Validation.validateSong(data)
        self.assertEqual(result["success"], True)


if __name__ == "__main__":
    unittest.main()
