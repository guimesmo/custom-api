from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class UserRegister(Resource):

    def post(self):
        """
        email
        password
        first name
        last name
        :return:
        """
        return dict(), 204


class ListCreate(Resource):
    def post(self):
        pass


class List(Resource):
    def get(self, list_id):
        pass

    def delete(self, list_id):
        pass

    def post(self, list_id):
        pass


class TodoItem(Resource):
    def put(self, list_id, todo_id):
        pass

    def delete(self, list_id, todo_id):
        pass


api.add_resource(UserRegister, '/register')
api.add_resource(ListCreate, '/list')
api.add_resource(List, '/list/<int:list_id>')
api.add_resource(TodoItem, '/list/<int:list_id>/<int:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)