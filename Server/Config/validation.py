from kanpai import Kanpai


class Validation:

    @staticmethod
    def validateSong(requestBody):
        schema = Kanpai.Object({
            "audiotype": Kanpai.String(error="audio type must be a string").required(error="audiotype is required"),
            "metadata": Kanpai.Object({
                "name": Kanpai.String(error="Song name must be a string").max(100).required(error="name is required"),
                "duration": Kanpai.Number(error="duration must be an int").required(error="duration is required")
            }).required(error="metadata is required")
        }).required(error="Invalid request body passed")

        valid_result = schema.validate(requestBody)
        return valid_result

    @staticmethod
    def validatePodcast(requestBody):
        schema = Kanpai.Object({
            "audiotype": Kanpai.String(error="audio type must be a string").required(error="audiotype is required"),
            "metadata": Kanpai.Object({
                "name": Kanpai.String(error="podcast name must be a string").max(100).required(error="name is required"),
                "duration": Kanpai.Number(error="duration must be an int").required(error="duration is required"),
                "host": Kanpai.String(error="host must be a string").max(100).required(error="host is required"),
                "participants": Kanpai.Array(error="participants must be a list").max(10)
            }).required(error="metadata is required")
        }).required(error="Invalid request body passed")

        valid_result = schema.validate(requestBody)
        return valid_result

    @staticmethod
    def validateAudiobook(requestBody):
        schema = Kanpai.Object({
            "audiotype": Kanpai.String(error="audio type must be a string").required(error="audiotype is required"),
            "metadata": Kanpai.Object({
                "title": Kanpai.String(error="audiobook title must be a string").max(100).required(error="title is required"),
                "author": Kanpai.String(error="author must be a string").max(100).required(error="author is required"),
                "narrator": Kanpai.String(error="narrator must be a string").max(100).required(error="narrator is required"),
                "duration": Kanpai.Number(error="duration must be an int").required(error="duration is required")
            }).required(error="metadata is required")
        }).required(error="Invalid request body passed")

        valid_result = schema.validate(requestBody)
        return valid_result
