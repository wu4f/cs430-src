# REPL example
# Via the import of os, you open your site up for all sorts of goodness like
#   os.popen('cat /etc/passwd').read()
import flask
import os
from util import login_required
class Repl(flask.views.MethodView):
    @login_required
    def get(self):
        return flask.render_template('repl.html')

    @login_required
    def post(self):
        result = eval(flask.request.form['expression'])
        flask.flash(result)
        return self.get()
