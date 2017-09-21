import web
import sqlite3 as sql
from validate_email import validate_email
render = web.template.render('templates/')

class home:
    def GET(self):
        """Send the server welcome.html page (found in templates/)"""
        return render.welcome()
