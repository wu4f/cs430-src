import flask, flask.views
import auth
from main import Main
from repl import Repl
from test import Test

app = flask.Flask(__name__)
app.secret_key = auth.secret_key

app.add_url_rule('/',
                 view_func=Main.as_view('index'),
                 methods=["GET", "POST"])

app.add_url_rule('/repl/',
                 view_func=Repl.as_view('repl'),
                 methods=['GET', 'POST'])

app.add_url_rule('/test/',
                 view_func=Test.as_view('test'),
                 methods=['GET'])

app.debug = True
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
