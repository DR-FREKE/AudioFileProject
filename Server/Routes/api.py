from flask import Blueprint, request, jsonify
from Controller.Main import Main


def routehandler():
    router = Blueprint('audio', __name__)
    main = Main()

    @router.route("/create-audio", methods=["POST"])
    def create():
        return main.add()

    @router.route("/delete-audio/<string:audioFileType>/<string:audioFileID>", methods=["DELETE"])
    def delete(audioFileType, audioFileID):
        return main.delete(audioFileType, audioFileID)

    @router.route("/update-audio/<string:audioFileType>/<string:audioFileID>", methods=["PUT"])
    def update(audioFileType, audioFileID):
        return main.update(audioFileType, audioFileID)

    @router.route("/get-audio/<string:audioFileType>", defaults={"audioFileID": None})
    @router.route("/get-audio/<string:audioFileType>/<string:audioFileID>")
    def read(audioFileType, audioFileID):
        return main.read(audioFileType, audioFileID)

    return router
