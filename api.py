from flask import Flask
from flask_restful import Api, Resource, reqparse, request
import db


app1 = Flask(__name__)
api = Api(app1)


class Students(Resource):
    def get(self):
        return db.get_students()


class Name(Resource):

    def get(self):

        email = request.form['email']
        return db.get_name(email)


api.add_resource(Students, "/students")
api.add_resource(Name, "/name")

if __name__ == "__main__":
    app1.run('0.0.0.0')
