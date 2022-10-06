from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from Config import Config
from extensions import db
from resources.user import UserListResource
from resources.instruction import InstructionListResource, InstructionResource


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app) #this will initialize the SQLALchemy and set up flask migrate
    register_resources(app) #resource routing

    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)


def register_resources(app):
    api = Api(app)

    api.add_resource(UserListResource, '/users')
    api.add_resource(InstructionListResource, '/instructions')
    api.add_resource(InstructionResource, '/instruction/<int:instruction_id>')


if __name__ == '__main__':
    app = create_app()
    app.run()