import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('shopkeeper.db')
c = conn.cursor()

# Create products table
c.execute('''CREATE TABLE IF NOT EXISTS products
             (product_no INTEGER PRIMARY KEY, 
              product_name TEXT, 
              selling_price REAL)''')

conn.commit()
conn.close()
