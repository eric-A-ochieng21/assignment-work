import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

def add_product():
    conn = sqlite3.connect('shopkeeper.db')
    c = conn.cursor()
    c.execute("INSERT INTO products (product_no, product_name, selling_price) VALUES (?, ?, ?)",
              (product_no_entry.get(), product_name_entry.get(), selling_price_entry.get()))
    conn.commit()
    conn.close()
    display_products()

def display_products():
    conn = sqlite3.connect('shopkeeper.db')
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    rows = c.fetchall()
    conn.close()
    
    for row in product_list.get_children():
        product_list.delete(row)
        
    for row in rows:
        product_list.insert("", tk.END, values=row)

def calculate_total_profit():
    conn = sqlite3.connect('shopkeeper.db')
    c = conn.cursor()
    c.execute("SELECT SUM(selling_price) FROM products")
    total_profit = c.fetchone()[0]
    conn.close()
    messagebox.showinfo("Total Profit", f"Total Profit: {total_profit}")

app = tk.Tk()
app.title("Shopkeeper Program")

tk.Label(app, text="Product No:").grid(row=0, column=0)
product_no_entry = tk.Entry(app)
product_no_entry.grid(row=0, column=1)

tk.Label(app, text="Product Name:").grid(row=1, column=0)
product_name_entry = tk.Entry(app)
product_name_entry.grid(row=1, column=1)

tk.Label(app, text="Selling Price:").grid(row=2, column=0)
selling_price_entry = tk.Entry(app)
selling_price_entry.grid(row=2, column=1)

tk.Button(app, text="Add Product", command=add_product).grid(row=3, column=0, columnspan=2)

product_list = ttk.Treeview(app, columns=("product_no", "product_name", "selling_price"), show="headings")
product_list.heading("product_no", text="Product No")
product_list.heading("product_name", text="Product Name")
product_list.heading("selling_price", text="Selling Price")
product_list.grid(row=4, column=0, columnspan=2)

tk.Button(app, text="Calculate Total Profit", command=calculate_total_profit).grid(row=5, column=0, columnspan=2)

display_products()

app.mainloop()
