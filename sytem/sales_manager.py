from datetime import datetime
from product_manager import ProductManager
from customer_manager import CustomerManager

class SalesManager:
    def __init__(self, con):
        self.con = con
        self.cursor = con.cursor()
    
    def begin_sales(self, code_bar, cpf):
        customer = CustomerManager(self.con)
        customer_id = customer.recover_customer(cpf)

        if customer_id is None:
            print("Customer not found!")
            return
        
        sales_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.cursor.execute("INSERT INTO sales (sales_date, customer_id, total) VALUES (?, ?, ?)", (sales_date, customer_id, 0.0))

        sales_id = self.cursor.lastrowid
        total = self.cursor.execute("SELECT total from sales WHERE id=?", (sales_id,))

        product = ProductManager(self.con)
        myproduct = product.retrieve_product(code_bar)
        
        product_id = myproduct[0]
        unit_price = myproduct[5]
        
        self.cursor.execute("INSERT INTO itemsales (sales_id, product_id, unit_price) VALUES (?, ?, ?)", (sales_id, product_id, unit_price))

        total = total + unit_price

        self.cursor.execute("UPDATE sales SET total=? WHERE id=?", (total, sales_id))
        self.con.commit()