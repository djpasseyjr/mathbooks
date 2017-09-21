import web
import sqlite3 as sql
from validate_email import validate_email
render = web.template.render('templates/')

class admin:
    def GET(self):
        """Sends the server admin.html (found in templates/). The                                                   
           file admin.html contains several special commands for                                                    
           the textbook application."""
        return render.admin()
