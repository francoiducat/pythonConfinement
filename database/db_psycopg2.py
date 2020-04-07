import psycopg2


def create_table():
    conn = psycopg2.connect(
        "dbname='pydb' user='postgres' password='postgres' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect(
        "dbname='pydb' user='postgres' password='postgres' host='localhost' port='5432'")
    cur = conn.cursor()
    # WARNIN sql injection :
    # cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect(
        "dbname='pydb' user='postgres' password='postgres' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect(
        "dbname='pydb' user='postgres' password='postgres' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE from store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect(
        "dbname='pydb' user='postgres' password='postgres' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",
                (quantity, price, item))
    conn.commit()
    conn.close()


# create_table()


# insert("Water Glass", 10, 5)
#insert("Coffee Cup", 10, 5)

#delete("Coffee Cup")
update(11, 6, "Water Glass")

print(view())
