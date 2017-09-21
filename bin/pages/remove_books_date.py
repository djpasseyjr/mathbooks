import web
import sqlite3 as sql
from validate_email import validate_email
import datetime
render = web.template.render('templates/')

class remove_books_date:
    def GET(self):
        before_date = [web.input().year, web.input().mon, web.input().day]
        date_str = "/".join([before_date[1],before_date[2],before_date[0]])
        db = sql.connect("MathBooks")
        cur = db.cursor()
        entries = []
        info = []
        status = True

        try:
            before_date = map(int,before_date)
        except ValueError:
            status = False

        if before_date[0] < 2000:
            status = False
        if before_date[1] < 0 or before_date[1] > 12:
            status = False
        if before_date[2] > 31 or before_date[2] < 0:
            status = False

        if status:
            before_date = datetime.date(before_date[0],before_date[1],before_date[2])
            cur.execute("SELECT * FROM Books;")
            entries = cur.fetchall()

        for e in entries:
            e = map(str,e)
            entry_date = map(int,e[5].split("-"))
            entry_date = datetime.date(entry_date[0],entry_date[1],entry_date[2])

            if entry_date < before_date:
                info.append(e)

        db.commit()
        db.close()

        return render.remove_books_date(info,date_str,status)

    def POST(self):
        before_date = web.input().date
        before_date = map(int,before_date.split('/'))
        before_date = datetime.date(before_date[2],before_date[0],before_date[1])
        
        db = sql.connect("MathBooks")
        cur = db.cursor()
        cur.execute("SELECT * FROM Books;")
        entries = cur.fetchall()
        info = []

        for e in entries:
            e = map(str,e)
            entry_date = map(int,e[5].split("-"))
            entry_date = datetime.date(entry_date[0],entry_date[1],entry_date[2])

            if entry_date < before_date:
                print (e[0],e[3])
                cur.execute("""DELETE FROM Books WHERE Name IS "{}" AND ID IS {} AND Class IS "{}" AND Title is "{}" AND Email IS "{}";""".format(e[0],e[1],e[2],e[3],e[4]))
        
        db.commit()
        db.close()
        
        return render.remove_student_confirm()
