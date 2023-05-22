#user postgres
#password postgres
#port 5432

import psycopg2


def create_table():
    #This is the default db that can be accessed in pgAdmin
    #pgAdmin is where you can add or delete dbs from
    #data_conn = psycopg2.connect("postgres.db")
    data_conn = psycopg2.connect("dbname='testDb',user='postgres',password='postgres'")
    cursor = data_conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INT, price REAL)"
    )
    data_conn.connit()
    data_conn.close()


def insert(item, quantity, price):
    data_conn = psycopg2.connect("lite.db")
    cursor = data_conn.cursor()
    cursor.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
    data_conn.connit()
    data_conn.close()


def viewAll():
    data_conn = psycopg2.connect("lite.db")
    cursor = data_conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    data_conn.close()
    return rows


def delete(item):
    data_conn = psycopg2.connect("lite.db")
    cursor = data_conn.cursor()
    cursor.execute("DELETE FROM store WHERE item=?", (item, ))
    data_conn.connit()
    data_conn.close()


def deleteAll():
    data_conn = psycopg2.connect("lite.db")
    cursor = data_conn.cursor()
    cursor.execute("DELETE FROM store")
    data_conn.connit()
    data_conn.close()
    print("Everything Deleted")


def update(quantity, price, item):
    data_conn = psycopg2.connect("lite.db")
    cursor = data_conn.cursor()
    cursor.execute("UPDATE store SET quantity=?, price=? WHERE item=?",
                   (quantity, price, item))
    data_conn.connit()
    data_conn.close()


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
