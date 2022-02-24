import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)

from main_app import app
import json


def test_hello():
    response = app.test_client().get('/hello_world')
    res = json.loads(response.data.decode('utf-8'))

    assert type(res) is dict
    assert type(res.get("message")) is str
    assert res.get("message") == "Hello world"

def test_create_succ():
    response = app.test_client().post('/employee/create', 
        data=json.dumps({
            'name': 'amine',
            'age': 24,
            'position' : 'Software Data Engineer'}),
        content_type='application/json',
        )
    res = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert type(res.get('data')) is int
    assert res.get('message') == "OK"

def test_create_fail():
    response = app.test_client().post('/employee/create', 
        data=json.dumps({
            'name_': 'ahmed',
            'age_': 25,
            'position' : 'Data Scientist',
            'another_field' : 'somthing went wrong'
            }),
        content_type='application/json',
        )
    res = json.loads(response.data.decode('utf-8'))


    assert response.status_code == 400
    assert res.get('message') == "There is a problem !"

def test_get_all():
    response = app.test_client().get('/employees')
    res = json.loads(response.data.decode('utf-8'))

    assert type(res.get('data')) is list
    assert type(res.get('data')[0]) is dict
    assert response.status_code == 200


if __name__ == '__main__':
    test_hello()
    test_create_succ()
    test_create_fail()
    test_get_all()