
m flask import make_response, abort
import gbmodel
import json

def entries(request):
    """ Guestbook API endpoint
        :param request: flask.Request object
        :return: flask.Response object (in JSON), HTTP status code
    """
    model = gbmodel.get_model()
    if request.method == 'GET':
        entries = [dict(name=row[0], email=row[1], date=str(row[2]), message=row[3] )
                       for row in model.select()]

        response = make_response(json.dumps(entries))
        response.headers['Content-Type'] = 'application/json'
        return response, 200

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
            model = gbmodel.get_model()
            model.insert(request_json['name'], request_json['email'], request_json['message'])
        else:
            raise ValueError("JSON missing name, email, or message property")

        response = make_response(request_json)
        response.headers['Content-Type'] = 'application/json'
        return request_json, 201

    return abort(403)
