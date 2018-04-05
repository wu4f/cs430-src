from enum import Enum, unique
import typing

class PresentView:
    """docstring for ."""
    def __init__(self, route, flash=None):
        self.route = route
        self.flash = flash

    def get_route(self):
        return self.route

    def get_flash(self):
        return self.flash

    def equals(self, view):
        if (isinstance(view, PresentView) and
            (not ((self.get_flash() == None) or (view.get_flash() == None)))):
            return (self.get_route().equals(view.get_route())
                    and self.get_flash().equals(view.get_flash()))
        return False

class Route:
    """docstring for ."""
    def __init__(self, is_redir, pg_name, extra_args=None):
        self.is_redir = is_redir
        self.page_name = pg_name
        self.extra_args = extra_args

    def is_redirect(self):
        return self.is_redir

    def get_name(self):
        return self.page_name

    def get_args(self):
        return self.extra_args

    def equals(self, route):
        if (isinstance(route, Route) and
            (not ((self.get_args() == None) or (route.get_args() == None)))):
            return (self.is_redirect() == route.is_redirect()
                    and self.get_name() == route.get_name()
                    and self.get_args() == route.get_args())
        return False

class Flash:
    def __init__(self, msg , msg_type):
        self.msg = msg
        self.msg_type = msg_type

    def equals(self, flash):
        if (isinstance(flash, Flash)):
            return (self.get_msg() == flash.get_msg()
                    and self.get_msg_type() == flash.get_msg_type())
        return False

    def get_msg(self):
        return self.msg

    def get_msg_type(self):
        return self.msg_type

@unique
class MSG_TYPE(Enum):
    SUCCESS = 'success'
    FAIL = 'danger'
