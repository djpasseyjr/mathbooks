import sqlite3 as sql
import web

render = web.template.render('templates/')

class remove_student:
    def GET(self):
        id = str(web.input().id)

        status = True
        db = sql.connect("MathBooks")
        cur = db.cursor()
        name, email = "",""
        info = []

        try:
            if id[0] == "0":
                id = "1" + id
            id = int(id)
        except ValueError:
            status = False
        except IndexError:
            status = False
        
        if status:
            cur.execute("SELECT Name,Email FROM Books WHERE ID={}".format(id))
            query = cur.fetchone()
            print query
            if query != None and query != []:
                name, email = query[0],query[1]
                cur.execute("SELECT Class,Title FROM Books WHERE ID={}".format(id))
                info = cur.fetchall()
                for i in range(len(info)):
                    info[i] = map(str,info[i])
                    
            else:
                staus = False
                    
        db.close()
        id = str(id)[1:]

        return render.remove_student(name,email,info,status,id)

    def POST(self):
        id = str(web.input().id)
        if id[0] == "0":
            id = "1" + id

        status = False
        db = sql.connect("MathBooks")
        cur = db.cursor()
        cur.execute("DELETE FROM Books WHERE ID={}".format(id))
        db.commit()
        db.close()
        return render.remove_student_confirm()
