from random import randint
from flask import Flask
from flask_restful import Resource, Api
from quotes import QUOTES

app = Flask(__name__)
api = Api(app)


class DoSomething(Resource):
    """Returns a lovely quote to help you be motivated."""
    def get(self):
        return {'quote': QUOTES[randint(0, len(QUOTES) - 1)]}

api.add_resource(DoSomething, r'/quotes/', strict_slashes=False)

if __name__ == '__main__':
    app.run(debug=True)
