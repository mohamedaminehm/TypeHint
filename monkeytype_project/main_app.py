from flask import Flask, jsonify, request
from models import db
from service import Employee
from flask.wrappers import Response
from typing import Tuple


 
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/hello_world', methods= ['GET'])
def hello() -> Response:
    return jsonify(message = "Hello world")

@app.route('/employee/create', methods=['POST'])
def create_employe() -> Tuple[Response, int]:
    payload = request.json

    response = Employee().create(payload)
    if response:
        return jsonify(message= "OK" , data = response.id) , 200
    else:
        return jsonify(message= "There is a problem !"), 400



@app.route('/employees', methods=['GET'])
def get_all_employees() -> Tuple[Response, int]:
    response = Employee().get_all()
    if response:
        return jsonify(message='ok', data = response), 200


if __name__ == '__main__':
    app.run(host='localhost', port=5000,debug=True)