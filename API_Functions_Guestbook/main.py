from flask import make_response, abort
import gbmodel
import json

def gb(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
    Returns:
        response (flask.Response): The response object (in JSON)
    """
    if request.method == 'GET':
        model = gbmodel.get_model()
        entries = [dict(name=row[0], email=row[1], signed_on=str(row[2]), message=row[3] ) for row in model.select()]
        json_resp = { i:x for i,x in enumerate(entries,1)}
        response = make_response(json.dumps(json_resp))
        response.headers['Content-Type'] = 'application/json'
        return response
    if request.method == 'POST' and request.headers['content-type'] == 'application/json':
        request_json = request.get_json(silent=True)
        if all(key in request_json for key in ('name', 'email', 'message')):
            name = request_json['name']
        else:
            raise ValueError("JSON is invalid, or missing a property")
        return 'Hello {}!'.format(name)
    else:
        return abort(403)
