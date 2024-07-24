import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / 'supermarket_db.sqlite')

cur = con.cursor()

def create_table_products(con, cur):
    cur.execute("""
                CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name VARCHAR(100) NOT NULL, 
                brand VARCHAR(100) NOT NULL, 
                expiration_date TEXT NOT NULL, 
                department VARCHAR(100), 
                price REAL NOT NULL, 
                code_bar INTEGER UNIQUE
                )
    """)
    con.commit()

def create_table_stock(con, cur):
    cur.execute("""
                CREATE TABLE IF NOT EXISTS stock (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                product_id INTEGER NOT NULL,
                total_amount INTEGER NOT NULL,
                FOREIGN KEY(product_id) REFERENCES products(id)
                )
    """)
    con.commit()

def create_table_customers(con, cur):
    cur.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                cpf CHAR(11) UNIQUE NOT NULL, 
                name VARCHAR(100) NOT NULL, 
                birthday TEXT, 
                address VARCHAR(150), 
                phone_number VARCHAR(20)
                )
    """)
    con.commit()

def create_table_sales(con, cur):
    cur.execute("""
                CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                sales_date TEXT NOT NULL, 
                customer_id INTEGER NOT NULL, 
                total REAL,
                FOREIGN KEY(customer_id) REFERENCES customers(id)
                )
    """)
    con.commit()

def create_table_itemsales(con, cur):
    cur.execute("""
                CREATE TABLE itemsales (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                sales_id INTEGER NOT NULL, 
                product_id INTEGER NOT NULL, 
                unit_price REAL NOT NULL, 
                FOREIGN KEY(sales_id) REFERENCES sales(id), 
                FOREIGN KEY(product_id) REFERENCES products(id)
                )
    """)
    con.commit()

create_table_products(con, cur)
create_table_stock(con, cur)
create_table_customers(con, cur)
create_table_sales(con, cur)
create_table_itemsales(con, cur)

con.close()