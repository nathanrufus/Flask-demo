from flask import Flask,request,jsonify,current_app
import json
import sqlite3

app = Flask(__name__)

def db_connection():
    conn =None
    try:
        conn = sqlite3.connect('books.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn    


@app.route("/books",methods =["GET","POST"])
def books():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor= conn.execute("SELECT * FROM book")
        books=[
            dict(id=row[0],author=row[1],language=row[2],title=row[3])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)
    if request.method == "POST":
        new_author= request.form["author"]
        new_lan= request.form["language"]
        new_title= request.form["title"]
        sql = """INSERT INTO book(author,language,title)
                VALUES(?,?,?)"""
        cursor = cursor.execute(sql, (new_author,new_lan,new_title))
        conn.commit().app
        return f"Book with the id: {cursor.lastrowid} created successfully",201
if __name__ == '__main__':
    app.run(debug=True)