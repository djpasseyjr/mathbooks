import web
import sqlite3 as sql
from validate_email import validate_email
render = web.template.render('templates/')

class remove_books_class:
    def GET(self):
        given_class = str(web.input().given_class)
        class_str = given_class
        status = True
        db = sql.connect("MathBooks")
        cur = db.cursor()
        info = []
        
        given_class= given_class.split()
        try:
            given_class = int(given_class[-1])
        except ValueError:
            status = False
        except IndexError:
            status = False

        if status:
            given_class = "Math " +str(given_class)
            class_str = given_class
            cur.execute("SELECT * FROM Books WHERE Class IS '{}';".format(given_class))
            info = cur.fetchall()
            for i in range(len(info)):
                info[i] = map(str,info[i])

        if len(info) == 0:
            staus = False

        db.close()
        return render.remove_books_class(info,class_str,status)

    def POST(self):
        given_class = str(web.input().given_class)

        status = False
        db = sql.connect("MathBooks")
        cur = db.cursor()
        cur.execute("DELETE FROM Books WHERE Class IS'{}';".format(given_class))
        db.commit()
        db.close()

        return render.remove_student_confirm()

