import web
import sqlite3 as sql
from validate_email import validate_email
render = web.template.render('templates/')

class remove_links:
    def GET(self):
        return render.remove_links()
    def POST(self):
        pass
