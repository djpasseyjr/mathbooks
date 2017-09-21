import web
import sqlite3 as sql
from validate_email import validate_email
render = web.template.render('templates/')

class email_opt:
    def GET(self):
        """Send the server email_instruct.html (found in templates/)"""
        return render.email_options()
