#No need to install sqlite3 as it is included in python3
import sqlite3


def create_table():
    data_comm = sqlite3.connect("lite.db")
    cursor = data_comm.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INT, price REAL)"
    )
    data_comm.commit()
    data_comm.close()


def insert(item, quantity, price):
    data_comm = sqlite3.connect("lite.db")
    cursor = data_comm.cursor()
    cursor.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
    data_comm.commit()
    data_comm.close()


def viewAll():
    data_comm = sqlite3.connect("lite.db")
    cursor = data_comm.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    data_comm.close()
    return rows


def delete(item):
    data_comm = sqlite3.connect("lite.db")
    cursor = data_comm.cursor()
    cursor.execute("DELETE FROM store WHERE item=?", (item, ))
    data_comm.commit()
    data_comm.close()


def deleteAll():
    data_comm = sqlite3.connect("lite.db")
    cursor = data_comm.cursor()
    cursor.execute("DELETE FROM store")
    data_comm.commit()
    data_comm.close()
    print("Everything Deleted")


def update(quantity, price, item):
    data_comm = sqlite3.connect("lite.db")
    cursor = data_comm.cursor()
    cursor.execute("UPDATE store SET quantity=?, price=? WHERE item=?",
                   (quantity, price, item))
    data_comm.commit()
    data_comm.close()


#create_table()

insert("Wine Glass", 12, 12.50)
insert("Beer Glass", 6, 10.50)
insert("Tea Cup", 6, 3.50)

print(viewAll())
delete("Wine Glass")
delete("Beer Glass")
update(5, 4.50, "Tea Cup")
print(viewAll())
deleteAll()
print(viewAll())
