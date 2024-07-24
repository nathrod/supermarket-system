import sqlite3

class CustomerManager:
    def __init__(self, con):
        self.con = con
        self.cursor = con.cursor()
    
    def add_customer(self, cpf, name, birthday, address, phone_number):
        try:
            self.cursor.execute("INSERT INTO customers (cpf, name, birthday, address, phone_number) VALUES (?, ?, ?, ?, ?)", (cpf, name, birthday, address, phone_number))
            self.con.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    
    def recover_customer(self, cpf):
        self.cursor.execute("SELECT id FROM customers WHERE cpf=?", (cpf,))
        result = self.cursor.fetchone()
        return result[0] if result else None
    
    def remove_customer(self,cpf):
        try:
            self.cursor.execute("DELETE from customers WHERE cpf=?", (cpf,))
            self.con.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def change_customer_infos(self):
        pass