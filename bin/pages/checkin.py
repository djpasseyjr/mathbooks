import web
import sqlite3 as sql
from validate_email import validate_email
render = web.template.render('templates/')

class checkin:
    def GET(self):
        """Send the server the inform.html page (found in templates/)"""
        return render.inform()

    def POST(self):
        """Retrieve all books checked out by IDnum"""
        IDnum = web.input().id

        if IDnum[0] == "0":
            IDnum = "1" + IDnum

        status = True
        books = []
        name = ""

        try:
            IDnum = int(IDnum)
        except ValueError:
            status = False

        """Access database and retrieve information"""
        
        db = sql.connect("MathBooks")
        cur = db.cursor()
        if status:
            cur.execute("SELECT Title FROM BOOKS  WHERE ID is {};".format(IDnum))
            books = cur.fetchall()
        
            """Turn SQL Query into a string"""
            if books != []:
                for i in range(len(books)):
                    books[i] = str(i+1)+" - " + str(books[i][0])
                cur.execute("SELECT Name FROM Books WHERE ID is {}".format(IDnum))
                name = str(cur.fetchone()[0])
            else:
                status = False    

        db.close()

        IDnum = str(IDnum)[1:]
        """Send the server books_out.html (found in templates/)"""
        return render.books_out(books,status,IDnum,name)
