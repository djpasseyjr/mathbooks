import web
import sqlite3 as sql
from validate_email import validate_email
render = web.template.render('templates/')


class table:
    def GET(self):
        """Print out all the students who have books out in a big                                                   
           table. Get the information from the database, then send                                                  
           the server table.html (found in templates/)"""
        status = False
        db = sql.connect("MathBooks")
        cur = db.cursor()

        cur.execute("SELECT * FROM Books")
        info = cur.fetchall()
        for i in range(len(info)):
            info[i] = map(str,info[i])
            if len(info[i][1]) == 10:
                info[i][1] = info[i][1][1:]

        db.close()
        status = True

        return render.table(info,status)
