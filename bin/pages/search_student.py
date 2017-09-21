import sqlite3 as sql
import web

render = web.template.render('templates/')

class search_student:
    def GET(self):
        return render.search_student()
    def POST(self):
        pass
