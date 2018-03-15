from flask import session, logging, request
from passlib.hash import sha256_crypt
from functools import wraps

from view_header import Route, PresentView, Flash, MSG_TYPE

class Presenter:
    """docstring for ."""
    def __init__(self, model):
        self.model = model

    # Index
    def index(self):
        return 'home.html'

    def about(self):
        return 'about.html'

    #Articles
    def articles(self):
        articles = self.model.fetchall('articles')
        if articles[0]:
            args = {'articles':articles[1]}
            route = Route(False, 'articles.html', args)
            return PresentView(route)
        else:
            msg = 'No article found'
            args = {'msg':msg}
            route = Route(False, 'articles.html', args)
            return PresentView(route)

    #Single Article
    def article(self, id):
        article = self.model.art('articles', id)
        args = {'article':article}
        route = Route(False, 'article.html', args)
        return PresentView(route)

    def register(self, can_register, form):
        if can_register:
            name = form.name.data
            email = form.email.data
            username = form.username.data
            password = sha256_crypt.encrypt(str(form.password.data))
            if self.model.user_exists(name):
                route = Route(True, 'register')
                flash = Flash('Username {0} already exists.'.format(username), MSG_TYPE.FAIL)
                return PresentView(route, flash)
            else:
                self.model.register_user((name, email, username, password))
                route = Route(True, 'login')
                flash = Flash('You have registered.', MSG_TYPE.SUCCESS)
                return PresentView(route, flash)
        args = {'form':form}
        route = Route(False, 'register.html', args)
        return PresentView(route)

    #login
    def login(self, request_method, request_form):
        if request_method:
            username = request_form['username']
            password_candidate = request_form['password']
            can_login = self.model.auth_login(username, password_candidate)
            if can_login[0]:
                #compare password
                if can_login[1]:
                    session['logged_in'] = True
                    session['username'] = username
                    flash = Flash('You are now logged in.', MSG_TYPE.SUCCESS)
                    route = Route(True, 'dashboard')
                    return PresentView(route, flash)
                else:
                    error = {'error':'Invalid login'}
                    route = Route(False, 'login.html', error)
                    return PresentView(route)
            else:
                error = {'error':'USER DOES NOT EXIST!'}
                route = Route(False, 'login.html', error)
                return PresentView(route)
        route = Route(False, 'login.html')
        return PresentView(route)

    def logout(self):
        flash = Flash('You are now logged out.', MSG_TYPE.SUCCESS)
        route = Route(True, 'login')
        return PresentView(route, flash)

    # Dashboard
    def dashboard(self):
        articles = self.model.fetchall('articles')
        if articles[0]:
            args = {'articles':articles[1]}
            route = Route(False, 'dashboard.html', args)
            return PresentView(route)
        else:
            args = {'msg':'No article found'}
            route = Route(False,'dashboard.html', args)
            return PresentView(route)

    def add_article(self, can_add_art, form):
        if can_add_art:
            title = form.title.data
            body = form.body.data
            link = form.link.data

            self.model.add_art((title, body, session['username'], link))
            flash = Flash('Article created', MSG_TYPE.SUCCESS)
            route = Route(True, 'dashboard')
            return PresentView(route, flash)
        args = {'form':form}
        route = Route(False, 'add_article.html', args)
        return PresentView(route)

    def edit_article(self, id, can_edit, form):

        article = self.model.art('articles', id)
        form.title.data = article['title']
        form.body.data = article['body']

        if can_edit:
            title = request.form['title']
            body = request.form['body']

            self.model.update_art((title, body, id))
            flash = Flash('Article Updated', MSG_TYPE.SUCCESS)
            route = Route(True, 'dashboard')
            return PresentView(route, flash)
        args = {'form':form}
        route = Route(False, 'edit_article.html', args)
        return PresentView(route)

    def delete_article(self, id):
        self.model.delete_art(id)
        flash = Flash('Article Deleted', MSG_TYPE.SUCCESS)
        route = Route(True, 'dashboard')
        return PresentView(route, flash)
