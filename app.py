#!/usr/bin/python
from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

'''@app.route('/hosts',methods=['GET'])
def index():
    return "hello world"
'''
class TaskListAPI(Resource):
    def get(self):
        return "hello world"
api.add_resource(TaskListAPI,'/hosts',endpoint='host')
if __name__ == '__main__':
    app.run(debug=True)
