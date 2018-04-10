import sys

import site

sys.path.insert(0,'/var/www/html/itscs201/www')

site.addsitedir('/var/www/html/itscs201/www/env/lib/python3.5/site-packages')

activate_this = '/var/www/html/itscs201/www/env/bin/activate_this.py'

execfile(activate_this, dict(__file__=activate_this))



from app import app as application
