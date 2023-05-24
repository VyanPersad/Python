import sqlite3


class Database:
    #You essentially make the connect function a constructorby using __init__
    #You also need to pass self for all the functions.
    #For all methods the close attribute is commented out as if not then on
    #executing the database will close preventing further access.
    def __init__(self, db):
        self.data_conn = sqlite3.connect(db)
        self.cursor = self.data_conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)"
        )
        self.data_conn.commit()
        #We don't close it as when we call the class we leave it open now thus
        #for every other method we don't have to re-open the connection
        #data_conn.close()

    def insert(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",
                            (title, author, year, isbn))
        self.data_conn.commit()
        #self.data_conn.close()

    def view(self):
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        #self.data_conn.close()
        return rows

    def delete(self, id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (id, ))
        self.data_conn.commit()
        #self.data_conn.close()

    def deleteAll(self):
        self.cursor.execute("DELETE FROM books")
        self.data_conn.commit()
        #self.data_conn.close()
        print("Everything Deleted")

    def update(self, id, title, author, year, isbn):
        if (id):
            self.cursor.execute(
                #The id goes last here as the order in the brackets must
                #match the order in the sql statement.
                #The order of the function params doesn't mater here.
                "UPDATE books SET title=?, author=?, year=?,isbn=? WHERE id=?",
                #The order here must be the same as the SQL statement above.
                (title, author, year, isbn, id))
            self.data_conn.commit()
            #self.data_conn.close()
        else:
            print("That book does not exist. Would you like to add it?")
            user_input = input("Yes (Y) or No (N) :")
            print(user_input)
            if (user_input == 'Y'):
                title = input("Insert Title: ")
                author = input("Insert Author: ")
                year = input("Insert Year: ")
                isbn = input("Insert ISBN: ")
                self.insert(title, author, year, isbn)

    def search(self, title="", author="", year="", isbn=""):
        self.cursor.execute(
            "SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",
            (title, author, year, isbn))
        rows = self.cursor.fetchall()
        #self.data_conn.close()
        return rows

    def __del__(self):
        self.data_conn.close()


#You need to call the function to ensure that it is executed when called by frontend.
#Now we don't need these function as the __innit__ function automatically connects
#Database.connect()
#To test the functions
#Database.insert("Moby Dick", "John Smith", 1989, 15248)
#Database.insert("Pippy", "Enid Blyton", 2010, 14586)
#print(Database.view())
#Database.update(2, "Pippy 2", "Enid Blyton", 2015, 14587)
#Database.deleteAll()
#print(Database.view())