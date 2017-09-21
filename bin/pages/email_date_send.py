import sqlite3 as sql
from send_email_function import send_email
import web

render = web.template.render('templates/')

class email_date_send:
    def GET(self):
        
        db = sql.connect("MathBooks")
        cur = db.cursor()

        emails = set()
        status = True
        book_dict = {}
 
        cur.execute("SELECT email FROM to_email")
        for addr in cur.fetchall():
            emails.add(str(addr[0]))

        if emails == set():
            status = False

        if status:
            for addr in emails:
                cur.execute("SELECT title FROM to_email WHERE email='{}';".format(addr))
                books = []
                for title in cur.fetchall():
                    books.append(str(title[0]))
                book_dict[addr] = books

            send_email(book_dict,emails)

        cur.execute("DROP TABLE to_email;")
        db.commit()
        db.close()

        return render.email_date_send(status)

