import sqlite3


def connect():
    data_conn = sqlite3.connect("books.db")
    cursor = data_conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)"
    )
    data_conn.commit()
    data_conn.close()


def insert(title, author, year, isbn):
    data_conn = sqlite3.connect("books.db")
    cursor = data_conn.cursor()
    cursor.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",
                   (title, author, year, isbn))
    data_conn.commit()
    data_conn.close()


def view():
    data_conn = sqlite3.connect("books.db")
    cursor = data_conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    data_conn.close()
    return rows


def delete(id):
    data_conn = sqlite3.connect("books.db")
    cursor = data_conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (id, ))
    data_conn.commit()
    data_conn.close()


def deleteAll():
    data_conn = sqlite3.connect("books.db")
    cursor = data_conn.cursor()
    cursor.execute("DELETE FROM books")
    data_conn.commit()
    data_conn.close()
    print("Everything Deleted")


def update(id, title, author, year, isbn):
    if (id):
        data_conn = sqlite3.connect("books.db")
        cursor = data_conn.cursor()
        cursor.execute(
            #The id goes last here as the order in the brackets must
            #match the order in the sql statement.
            #The order of the function params doesn't mater here.
            "UPDATE books SET title=?, author=?, year=?,isbn=? WHERE id=?",
            #The order here must be the same as the SQL statement above.
            (title, author, year, isbn, id))
        data_conn.commit()
        data_conn.close()
    else:
        print("That book does not exist. Would you like to add it?")
        user_input = input("Yes (Y) or No (N) :")
        print(user_input)
        if (user_input == 'Y'):
            title = input("Insert Title: ")
            author = input("Insert Author: ")
            year = input("Insert Year: ")
            isbn = input("Insert ISBN: ")
            insert(title, author, year, isbn)


def search(title="", author="", year="", isbn=""):
    data_conn = sqlite3.connect("books.db")
    cursor = data_conn.cursor()
    cursor.execute(
        "SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",
        (title, author, year, isbn))
    rows = cursor.fetchall()
    data_conn.close()
    return rows


#You need to call the function to ensure that it is executed when called by frontend.
connect()
#To test the functions
#insert("Moby Dick", "John Smith", 1989, 15248)
#insert("Pippy", "Enid Blyton", 2010, 14586)
#print(view())
#update(2, "Pippy 2", "Enid Blyton", 2015, 14587)
#deleteAll()
#print(view())