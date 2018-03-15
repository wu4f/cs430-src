from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from functools import wraps
import requests

from model import AppModel
from view_header import Route
from presenter import Presenter
from form import ArticleForm, RegisterForm
from newsapi import News, NEWS_SRC

app = Flask(__name__)
model = AppModel(app)
presenter = Presenter(model)

def create_template(route):
    route_name = route.get_name()

    if route.is_redirect():
        return redirect(url_for(route_name))
    else:
        route_arg = route.get_args()
        if (route_arg == None):
            return render_template(route_name)
        return render_template(route_name, **(route_arg))

def present_flash(f):
    if (not (f == None)):
        flash(f.get_msg(), f.get_msg_type().value)

def render_view(view):
    present_flash(view.get_flash())
    return create_template(view.get_route())

# Index
@app.route('/')
def index():
    return render_template(presenter.index())

@app.route('/about')
def about():
    return render_template(presenter.about())
#Articles
@app.route('/news/articles')
def articles():
    return render_view(presenter.articles())

#Single Article
@app.route('/news/article/<string:id>/')
def article(id):
    return render_view(presenter.article(id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    can_reg = request.method == 'POST' and form.validate()
    return render_view(presenter.register(can_reg, form))

#login
@app.route('/login', methods=['GET', 'POST'])
def login():
    rm = request.method == 'POST'
    return render_view(presenter.login(rm, request.form))

# Check if user is logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized', 'danger')
            return redirect(url_for('login'))
    return wrap

#Log out
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    return render_view(presenter.logout())

# Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    return render_view(presenter.dashboard())

@app.route('/add_article', methods=['POST', 'GET'])
@is_logged_in
def add_article():
    form = ArticleForm(request.form)
    can_add = request.method == 'POST' and form.validate()
    print(request.method)
    print(form.validate())
    return render_view(presenter.add_article(can_add, form))

#Edit article
@app.route('/edit_article/<string:id>', methods=['POST', 'GET'])
@is_logged_in
def edit_article(id):
    form = ArticleForm(request.form)
    can_edit = request.method == 'POST' #and form.validate() # for some reason form stop validating, therefore it's comment out for edit to "work"
    # print(can_edit)
    # print(form.validate())
    return render_view(presenter.edit_article(id, can_edit, form))

@app.route('/delete_article/<string:id>', methods=['POST'])
@is_logged_in
def delete_article(id):
    return render_view(presenter.delete_article(id))

@app.route('/news')
def news():
    # return render_template('news.html', articles=art, err='error')
    news = News()
    aa = news.fetchall_arts(NEWS_SRC.BLOOMBERG.name)
    return render_template('news.html', articles=aa)

@app.route('/news/<string:name>')
def news_src(name):
    # return render_template('news.html', articles=art, err='error')
    news = News()
    aa = news.fetchall_arts(name)
    yo = {'articles':aa, 'source':name}
    print('HIIIII')
    print(name)
    return render_template('news.html', articles=aa, source=name)


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
