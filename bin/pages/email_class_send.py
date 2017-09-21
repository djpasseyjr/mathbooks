import sqlite3 as sql
from send_email_function import send_email
import web

render = web.template.render('templates/')

class email_class_send():
    def GET(self):
        given_class = web.input().given_class
        given_class = " ".join(given_class.split('&'))

        db = sql.connect("MathBooks")
        cur = db.cursor()

        email_set = set()
        book_dict = {}

        """Get all email addresses"""
        cur.execute("SELECT email FROM Books WHERE CLASS='{}';".format(given_class))
        for c in cur.fetchall():
            email_set.add(str(c[0]))

        """Get all books associated with the email address"""
        for addr in email_set:
            book_set = set()
            
            cur.execute("SELECT Title FROM Books WHERE Email='{}' AND Class='{}';".format(addr,given_class))
            for title in cur.fetchall():
                book_set.add(str(title[0]))
            
            book_dict[addr] = [book for book in book_set]

        print book_dict
        print [e for e in email_set]
        send_email(book_dict,[e for e in email_set])

        return render.email_class_send()
