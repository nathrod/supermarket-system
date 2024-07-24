import sqlite3

class ProductManager:
    def __init__(self, con):
        self.con = con
        self.cursor = con.cursor()
    
    def add_product(self,name, brand, expiration_date, department, price, code_bar):
        self.cursor.execute("SELECT * FROM products WHERE code_bar = ?", (code_bar,))
        if self.cursor.fetchone():
            print("Error: Bar code already exists in the system. ")
        else:
            self.cursor.execute("INSERT INTO products (name, brand, expiration_date, department, price, code_bar) VALUES (?, ?, ?, ?, ?, ?)", (name, brand, expiration_date, department, price, code_bar))
            self.con.commit()
            print("Product saved")
    
    def add_products(self, datas):
        self.cursor.executemany("INSERT INTO products (name, brand, expiration_date, department, price, code_bar) VALUES (?, ?, ?, ?, ?, ?)", datas)
        self.con.commit()

    #Only for cases when a product needs to be removed manually.
    def remove_product(self, id):
        self.cursor.execute("DELETE from products WHERE id=?",(id,))
        self.con.commit()

    def update_product(self,name, brand, expiration_date, department, price, code_bar, id):
        data = (name, brand, expiration_date, department, price, code_bar, id)
        self.cursor.execute("UPDATE products SET name=?, brand=?, expiration_date=?, department=?, price=?, code_bar=? WHERE id=?", data)
        self.con.commit()
    
    def retrieve_product(self,code_bar):
        self.cursor.execute("SELECT * FROM products WHERE code_bar=?", (code_bar,))
        return self.cursor.fetchone()