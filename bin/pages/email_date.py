import web
import sqlite3 as sql
from validate_email import validate_email
render = web.template.render('templates/')
import datetime 

class email_date:
    def GET(self):
        return render.email_instruct()
    def POST(self):
        status = True
        before_date = [web.input().year, web.input().mon, web.input().day]
        date_str = "/".join([before_date[1],before_date[2],before_date[0]])
        info = []
        entries = []
        db = sql.connect("MathBooks")
        cur = db.cursor()

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
        print before_date
        print status

        if status:
            before_date = datetime.date(before_date[0],before_date[1],before_date[2])

            cur.execute("SELECT * FROM Books;")
            entries = cur.fetchall()
            name_set,email_set = set(),set()        

        cur.execute("DROP TABLE IF EXISTS to_email;")
        cur.execute("CREATE TABLE to_email (Name TEXT, Title TEXT, Email TEXT)")

        for e in entries:
            e = map(str,e)
            entry_date = map(int,e[5].split("-"))
            entry_date = datetime.date(entry_date[0],entry_date[1],entry_date[2])

            if entry_date < before_date:
                row = [e[0],e[3],e[4]]
                cur.execute("INSERT INTO to_email VALUES(?,?,?);",row)
                name, email = row[0],row[2]

                if not (name in name_set or email in email_set):
                    info.append([name,email])
                    name_set.add(name)
                    email_set.add(email)
        db.commit()
        db.close()
            
        return render.email_date_table(info,date_str,status)
                
