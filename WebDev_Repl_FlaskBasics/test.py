import flask
from util import login_required
class Test(flask.views.MethodView):
    @login_required
    def get(self):
        return flask.render_template('test.html')
