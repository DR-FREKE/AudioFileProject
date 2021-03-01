from dataclasses import dataclass
from flask import jsonify


class Outputter:

    def toJSON(self, response):
        pass

    def success(self, response):
        response = {"success": True, "data": response, "error": None}
        return jsonify(response), 200

    def failure(self, response, code):
        response = {"success": False, "data": None, "error": response}
        return jsonify(response), code
