import web
import sqlite3 as sql
from validate_email import validate_email
render = web.template.render('templates/')

class email_class:
    def GET(self):
        return render.email_class()
    def POST(self):
        given_class = web.input().given_class
        class_str = given_class
        status = True
        names_emails = []
        no_space = ""
        raw_data = []
        db = sql.connect('MathBooks')
        cur = db.cursor()
        
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
            cur.execute("SELECT name, email FROM Books WHERE class='{}'".format(given_class))
            raw_data = cur.fetchall()


        if raw_data != None and raw_data != []:
            print ("Raw data", raw_data)
            name_set,email_set = set(),set()
            for r in raw_data:
                name = str(r[0])
                email = str(r[1])
                dup = False
                if name in name_set or email in email_set:
                    dup = True
                if not dup:
                    names_emails.append([name,email])
                    name_set.add(name)
                    email_set.add(email)
            no_space ='&'.join(given_class.split())
        else:
            status = False

        db.close()

        return render.email_class_table(names_emails,no_space,class_str,status)            
