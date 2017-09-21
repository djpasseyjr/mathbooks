import sqlite3 as sql
import web

render = web.template.render('templates/')

class search_class:
    def GET(self):
        return render.search()
    def post(self):
        pass
