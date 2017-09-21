import web
from send_email_function import send_email
import sqlite3 as sql

render = web.template.render('templates/')

class email_student_send:
    def GET(self):
        id = web.input().ID

        db = sql.connect("MathBooks")
        cur = db.cursor()
        cur.execute("SELECT email FROM Books WHERE ID IS {};".format(id))
        toaddr = str(cur.fetchone()[0])
        
        cur.execute("SELECT title FROM Books WHERE ID IS {};".format(id))
        titles = []
        book_dict = dict()

        for title in cur.fetchall():
            titles.append(str(title[0]))

        book_dict[toaddr] = titles
        db.close()
        
        send_email(book_dict,[toaddr])       

        return render.email_student_send()



        
        
