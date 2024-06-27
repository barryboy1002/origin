import sqlite3

# Connect to the database
conn = sqlite3.connect("Userdata.db")

def create_cursor(connector):
    """Create a new cursor object for the database connection."""
    cur = connector.cursor()
    return cur

def create_table(connection):
    """Creates a stock table if one does not exist."""
    connection.execute("""
    CREATE TABLE IF NOT EXISTS InventoryTable(
        Item_id INTEGER PRIMARY KEY AUTOINCREMENT ,
        Item_name TEXT VARCHAR(255) NOT NULL UNIQUE,
        No_Stock INTEGER NOT NULL DEFAULT 0,
        Price NUMERIC NOT NULL DEFAULT 0,
        Sales NUMERIC NOT NULL DEFAULT 0,
        Usage TEXT VARCHAR(255) ,
        Type TEXT VARCHAR(255)  )""")
    conn.commit()

def insert_static_data(name, usage, no_stock, type, price, connection):
    """Insert static variables into the database."""
    try:
        connection.execute("""
        INSERT INTO InventoryTable(Item_name, No_Stock, Usage, Type, Price) 
        VALUES(?, ?, ?, ?, ?)
        """, (name, no_stock, usage, type, price))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_dynamic_data(button,name,amount_sold,connection):
    """Update dynamic variables and change their values before inserting into the database."""
    if button:
        price_list  = connection.execute ("SELECT Item_name ,Price,No_stock FROM InventoryTable").fetchall()
        print(price_list)
        for items in price_list:
            if items[0] == name:
                if items[2]  > 0:
                    price = items[1]
                    connection.execute("""
                            UPDATE InventoryTable
                            SET Sales = Sales  + ?, No_Stock = No_Stock - ?
                            WHERE Item_name = ? 
                            """, (price, amount_sold, name))
                    conn.commit()
                else:
                    return "Out of stock!!!"
            else:
                return "Item does not exist in database."


def access_inventory(connection):
    """Access all the data to be modified."""
    the_list = connection.execute("""
        SELECT * FROM InventoryTable
        """).fetchall()
    return the_list

"""
# Test data
connection = create_cursor(conn)
#create_table(connection)

# update dynamic data
update_dynamic_data(True,"Sadaf",8,connection)
# Access inventory data
data_list = access_inventory(connection)

print(data_list)
"""
