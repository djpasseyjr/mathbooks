import web
import sqlite3 as sql
import datetime
from validate_email import validate_email
render = web.template.render('templates/')

class checkout:

    def GET(self):
        """Send the server the checkout.html page (found in templates/)"""
        return render.checkout()

    def POST(self):
        info = web.input()
        d = datetime.date.today()
        info = [info.name,info.ID,info.classname,info.book,info.email,str(d)]
        """Validate email address"""
        error_message = ''
        status = True
        blank = False
        UniqueID = True
        name = ''

        for i in info:
            if len(i) == 0:
                status = False
                blank = True
        if blank:
            error_message += "One or more blank fields. "


        if len(info[1]) != 9:
            status = False
            error_message += "ID must have 9 digits. "

        if status:
            if info[1][0] == "0":
                info[1] = "1" + info[1]

        try:
           info[1] = int(info[1])
        except ValueError:
            status = False
            error_message += "ID must be an Integer. "

        """Process Class"""
        info[2] = info[2].split()
        try:
            info[2] = int(info[2][-1])
        except ValueError:
            status = False
            error_message += "Invalid Class. "
        except IndexError:
            status = False
            error_message += "Invalid Class. "
        if status:
            info[2] = "Math " + str(info[2])


        """Validate email"""
        if not validate_email(info[4]):
            status = False
            error_message += "Invalid email. "

        db = sql.connect("MathBooks")
        cur = db.cursor()

        try:
            cur.execute("CREATE TABLE Books (Name TEXT, ID INTEGER NOT NULL, Class TEXT, Title TEXT, email TEXT,date TEXT);")
        except Exception:
           pass

        """Check for Unique ID"""
        if status:
            cur.execute("SELECT Name FROM Books WHERE ID={}".format(info[1]))
            try:
                name = str(cur.fetchone()[0])
                if name != info[0]:
                    status = False
                    UniqueID = False
            except TypeError:
                pass


        """Check for duplicates"""
        if status:
            cur.execute("""SELECT * FROM Books WHERE ID={} AND Class="{}" AND Title="{}";""".format(info[1],info[2],info[3]))
            duplicate=cur.fetchall()
            if duplicate != list():
                status = False
                error_message += "Entry already exists in database."

        if status:
            """Store the form input in a sql database 
               Send the server input status.html"""
            
            cur.execute("INSERT INTO Books VALUES(?,?,?,?,?,?);",info)
            db.commit()
            db.close()

        return render.input_status(status,error_message,UniqueID,name)
