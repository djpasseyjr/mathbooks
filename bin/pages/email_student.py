import web
import sqlite3 as sql
from validate_email import validate_email
render = web.template.render('templates/')

class email_student:
    def GET(self):
        return render.email_student()
    def POST(self):
        id = web.input().id
        status = True
        info = []


        try:
            if id[0] == "0":
                id = "1" + id
            id = int(id)
        except ValueError:
            status = False
        except IndexError:
            status = False

        
        """Retrive Student Info"""
        if status:
            db = sql.connect("MathBooks")
            cur = db.cursor()

            cur.execute("""SELECT Name, email FROM Books WHERE ID is {}""".format(id))
            entry = cur.fetchone()

            if entry != None and entry != []:
                for e in entry:
                    info.append(str(e))
            else:
                status = False

        return render.email_student_table(info,id,status)
