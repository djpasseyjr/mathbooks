#app.py

""" Application for textbook checkout and return
    Created by DJ Passey
    Property of the BYU Mathematics Department
    March 3, 2017                                                              
"""

import web
import sqlite3 as sql
import sys
from validate_email import validate_email
import pages

urls = (
    '/','pages.home',
    '/checkout', 'pages.checkout',
    '/checkin', 'pages.checkin',
    '/email', 'pages.email_opt',
    '/table', 'pages.table',
    '/admin','pages.admin',
    '/remove', 'pages.remove',
    '/emailstudent','pages.email_student',
    '/emailstudentsend','pages.email_student_send',
    '/emailclass', 'pages.email_class',
    '/emailclasssend', 'pages.email_class_send',
    '/emaildate', 'pages.email_date',
    '/emaildatesend','pages.email_date_send',
    '/search', 'pages.search_class',
    '/remove_links', 'pages.remove_links',
    '/remove_books_student', 'pages.search_student',
    '/remove_student', 'pages.remove_student',
    '/remove_books_class', 'pages.remove_books_class',
    '/remove_books_date', 'pages.remove_books_date',
    '/clear', 'pages.clear'
)

app = web.application(urls,globals())
render = web.template.render('templates/')

if __name__ == "__main__":
    app.run()
