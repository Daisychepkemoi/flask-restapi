# from ast import Pass
# from crypt import methods
# import json
# from pydoc import render_doc
# import sqlite3
# from urllib.parse import ParseResultBytes
# from flask import Flask, jsonify, request, render_template

# test=Flask(__name__)
# # book_list = [
    
# # {
# # 	"id": 0,
# # 	"author":"Chenua achebe0",
# # 	"language": "english",
# # 	"title": "things fall apart"
# # }, 
# # {
# # 	"id": 2,
# # 	"author":"Chenua achebe1",
# # 	"language": "english",
# # 	"title": "things fall apart"
# # }, 
# # {
# # 	"id": 3,
# # 	"author":"Chenua achebe2",
# # 	"language": "english",
# # 	"title": "things fall apart"
# # }, 
# # {
# # 	"id": 4,
# # 	"author":"Chenua achebe3",
# # 	"language": "english",
# # 	"title": "things fall apart"
# # }, 
# # {
# # 	"id": 5,
# # 	"author":"Chenua achebe4",
# # 	"language": "english",
# # 	"title": "things fall apart"
# # }, 
# # {
# # 	"id": 6,
# # 	"author":"Chenua achebe5",
# # 	"language": "english",
# # 	"title": "things fall apart"
# # }, 
# # {
# # 	"id": 7,
# # 	"author":"Chenua achebe6",
# # 	"language": "english",
# # 	"title": "things fall apart"
# # }, 
# # {
# # 	"id": 8,
# # 	"author":"Chenua achebe7",
# # 	"language": "english",
# # 	"title": "things fall apart"
# # }, 
# # {
# # 	"id": 9,
# # 	"author":"Chenua achebe8",
# # 	"language": "english",
# # 	"title": "things fall apart"
# # }, 
# # {
# # 	"id": 10,
# # 	"author":"Chenua achebe9",
# # 	"language": "english",
# # 	"title": "things fall apart"
# # }, 


# # ]



# def db_connection():
#     conn = None
#     try:
#         conn = sqlite3.connect('books.sqlite')
#     except sqlite3.error as e:
#         print(e)
#     return conn


# @test.route("/")
# def index():
#     # """Print 'Hello, world!' as the response body."""
#     return "Hello World"

# @test.route("/books", methods=["GET", "POST"])
# def books():
#     conn = db_connection()
#     cursor = conn.cursor()
#     if(request.method == 'GET'):
#         cursor = conn.execute("SELECT * FROM Book")
#         books = [
#             dict(id = row[0], author = row[1], language=row[2], title=row[3])
#             for row in cursor.fetchall()
#         ]
#         if books is not None:
#             return jsonify(books)
        
      
#     if request.method == 'POST' :
#         new_author = request.form['author']
#         new_language = request.form['language']
#         new_title = request.form["title"]
#         sql = """INSERT INTO Book (author,language,title) VALUES (?,?,?)"""

#         cursor = conn.execute(sql,(new_author,new_language,new_title))
#         conn.commit()
#         return f"Book with id: {cursor.lastrowid} created successfully", 201
        
# @test.route("/book/<int:id>", methods=["GET", "PUT","DELETE"])
# def single_book(id):
#     conn = db_connection()
#     cursor = conn.cursor()
#     if request.method == 'GET':
#         sql = """SELECT * FROM Book where id=?"""
#         cursor.execute(sql,(id,))
#         rows = cursor.fetchall()
#         for r in rows:
#             book = r
#         if book is not None:
#             return jsonify(book), 200
#         else:
#             return f"Books not found", 400
#     if(request.method == 'PUT'):

#         updated_author = request.form['author']
#         updated_language = request.form['language']
#         updated_title = request.form["title"]
#         updated_book ={
#             "id": id,
#             "author": updated_author,
#             "language": updated_language,
#             "title": updated_title
#         }
#         sql = """UPDATE Book set author = ? , language = ?, title = ? where id = ?"""
#         cursor.execute(sql,(updated_author,updated_language,updated_title,id))
#         conn.commit() 

#         return  jsonify(updated_book), 201
       
#     if request.method == 'DELETE':
         
#           sql = """DELETE FROM Book where id = ?"""
#           cursor.execute(sql,(id,))
#           conn.commit()
#           return f"book with id {id}  deleted successfully", 200
  

# @test.route("/<name>")
# def print_name(name):
#     return render_template("index.html", username = name)

# # if __name__ == '__main__':
# #     test.run(debug=True)
