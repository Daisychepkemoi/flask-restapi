from ast import Pass
from crypt import methods
import json
from pydoc import render_doc
import pymysql
from urllib.parse import ParseResultBytes
from flask import Flask, jsonify, request, render_template
from service.database.db_connect import db_connect 

py_my_sql_app=Flask(__name__)

def db_connection():
    conn = None
    try:
         conn = db_connect.connect()
    except pymysql.error as e:
        print(  e)
    return conn


@py_my_sql_app.route("/")
def index():
    
    return "Hello World"

@py_my_sql_app.route("/books", methods=["GET", "POST"])
def books():
    conn = db_connection()
   
    cursor = conn.cursor()
    books = None
    if(request.method == 'GET'):
        cursor.execute("SELECT * FROM Book")
        books = [
            dict(id = row['id'], author = row['author'], language=row['language'], title=row['title'])
            for row in cursor.fetchall()
        ]
       
        if books is None:
            return "No book found"
            
        else :
          return jsonify(books)
        
      
    if request.method == 'POST' :
        new_author = request.form['author']
        new_language = request.form['language']
        new_title = request.form["title"]
        sql = """INSERT INTO Book (author,language,title) VALUES (%s,%s,%s)"""

        cursor.execute(sql,(new_author,new_language,new_title))
        conn.commit()
        return f"Book with id: {cursor.lastrowid} created successfully", 201
        
@py_my_sql_app.route("/book/<int:id>", methods=["GET", "PUT","DELETE"])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    book = None
    print( book)
    if request.method == 'GET':
        sql = """SELECT * FROM Book where id=%s"""
        cursor.execute(sql,(id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is None:
                
                return "Book not found", 400
                
        else:
                return jsonify(book), 200
    if(request.method == 'PUT'):

        updated_author = request.form['author']
        updated_language = request.form['language']
        updated_title = request.form["title"]
        updated_book ={
            "id": id,
            "author": updated_author,
            "language": updated_language,
            "title": updated_title
        }
        sql = """UPDATE Book set author = %s , language = %s, title = %s where id = %s"""
        cursor.execute(sql,(updated_author,updated_language,updated_title,id))
        conn.commit() 

        return  jsonify(updated_book), 201
       
    if request.method == 'DELETE':
         
          sql = """DELETE FROM Book where id = %s"""
          cursor.execute(sql,(id,))
          conn.commit()
          return f"book with id {id}  deleted successfully", 200
  

@py_my_sql_app.route("/<name>")
def print_name(name):
    return render_template("index.html", username = name)

if __name__ == '__main__':
    py_my_sql_app.run(debug=True)
