from flask import make_response, abort
import gbmodel
import json

def handle_cors(method):
    response = make_response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = method
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Max-Age'] = '3600'
    return response

def entries(request):
    """ Guestbook API endpoint
        :param request: flask.Request object
        :return: flask.Response object (in JSON), HTTP status code
    """
    model = gbmodel.get_model()
    if request.method == 'GET':
        entries = [dict(name=row[0], email=row[1], date=str(row[2]), message=row[3] ) for row in model.select()]
        response = make_response(json.dumps(entries))
        response.headers['Content-Type'] = 'application/json'
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response, 200

    if request.method == 'OPTIONS':
        return handle_cors('GET'), 200

    return abort(403)

def entry(request):
    """ Guestbook API endpoint
        :param request: flask.Request object
        :return: flack.Response object (in JSON), HTTP status code
    """
    model = gbmodel.get_model()

    if request.method == 'POST' and request.headers['content-type'] == 'application/json':
        request_json = request.get_json(silent=True)

        if all(key in request_json for key in ('name', 'email', 'message')):
            model.insert(request_json['name'], request_json['email'], request_json['message'])
        else:
            raise ValueError("JSON missing name, email, or message property")

        entries = [dict(name=row[0], email=row[1], date=str(row[2]), message=row[3] ) for row in model.select()]
        response = make_response(json.dumps(entries))
        response.headers['Content-Type'] = 'application/json'
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response, 200

    if request.method == 'OPTIONS':
        return handle_cors('GET'), 200

    return abort(403)
