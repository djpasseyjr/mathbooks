import web
import sqlite3 as sql
from validate_email import validate_email
render = web.template.render('templates/')

class remove:
    def GET(self):
        status = False
        return render.return_status(status)

    def POST(self):
        """Get the web input"""
        book = int(web.input().b[0])
        id = web.input().ID
        if id[0] == "0":
            id = "1" + id

        status = True

        """Remove the selected book from the database"""
        db = sql.connect("MathBooks")
        cur = db.cursor()

        """Retrieve the book's title"""
        cur.execute("SELECT Title FROM Books WHERE ID LIKE ?",("%"+id+"%",))
        title = str(cur.fetchall()[book-1][0])
        print title
        cur.execute("DELETE FROM Books WHERE ID={} AND Title='{}';".format(id,title))

        db.commit()
        db.close()

        """Send the server return_status.html (found in templates/)"""
        return render.return_status(status)

