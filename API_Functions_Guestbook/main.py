from flask import make_response, abort
import gbmodel
import json

def gb(request):
    """ Guestbook API endpoint
        :param request: flask.Request object
        :return: flack.Response object (in JSON), HTTP status code
    """
    model = gbmodel.get_model()
    if request.method == 'GET':
        entries = [dict(name=row[0], email=row[1], signed_on=str(row[2]), message=row[3] )
                       for row in model.select()]

        entries_dict = { i:x for i,x in enumerate(entries,1)}

        response = make_response(json.dumps(entries_dict))
        response.headers['Content-Type'] = 'application/json'
        return response, 200

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
