import web
import sqlite3 as sql
from validate_email import validate_email
render = web.template.render('templates/')

class clear:
    def GET(self):
        return render.clear()
    def POST(self):
        db = sql.connect("MathBooks")
        cur = db.cursor()
        cur.execute("DROP TABLE Books")
        cur.execute("CREATE TABLE Books (Name TEXT, ID INTEGER NOT NULL, Class TEXT, Title TEXT, email TEXT,date TEXT);")
        db.commit()
        db.close()
        return render.remove_student_confirm()
