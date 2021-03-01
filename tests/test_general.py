import unittest


class TestAudio(unittest.TestCase):

    def test_audiotype_in_tuple(self):
        """ test audion type is in tuple """

        tuple_type = ("Song", "Podcast", "Audiobook")

        data = {
            "audiotype": "Audiobook",
            "metadata": {
                "duration": 37477,
                "title": "another",
                "author": "Solomon",
                "narrator": "Ndiferke"
            }
        }

        result = data["audiotype"]
        self.assertIn(result, tuple_type)

    def test_audiotype_not_empty(self):
        """ test that audio type is not empty """

        data = {
            "audiotype": "Audiobook",
            "metadata": {
                "duration": 37477,
                "title": "another",
                "author": "Solomon",
                "narrator": "Ndiferke"
            }
        }
        result = data["audiotype"]
        self.assertTrue(result)
