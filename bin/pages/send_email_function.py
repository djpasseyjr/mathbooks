import sqlite3 as sql
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def send_email(dict_books,address):

    db = sql.connect("MathBooks")
    cur = db.cursor()
    fromaddr = "noreply@mathematics.byu.edu"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr,"byumathfaculty")
    
    for toaddr in address:

        msg = MIMEMultipart()
        msg['To'] = toaddr
        msg['From'] = fromaddr
        msg['Subject'] = "Math Textbook Return"
        bodystart = "Dear {},\n\nYou have the following textbooks checked out from the BYU Mathematics Department:\n"
        bodyend = "\n\nTextbooks need to be renewed or returned at the end of each semester. Renew or return your textbook with Lonette Stoddard in TMCB 276. Failure to renew or return may result in charges to your student account.\n\nEmail lonettes@byu.edu with questions or concerns.\n\nThank you!\nBYU MATHEMATICS DEPARTMENT"

        for book in dict_books[toaddr]:
            bodystart += ('\n'+book)

        cur.execute("SELECT name FROM Books WHERE Email='{}';".format(toaddr))
        name =str(cur.fetchone()[0])
        body = bodystart.format(name)+bodyend

        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server.sendmail(fromaddr,toaddr,text)
    
    server.quit()
    db.close()
