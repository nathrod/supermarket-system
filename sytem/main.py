import sqlite3
from pathlib import Path
from product_manager import ProductManager
from sales_manager import SalesManager
from customer_manager import CustomerManager

ROOT_PATH = Path(__file__).parent

def menu_checkout():
    print("""
        1. Begin sale
        2. Register Customer
        0. Exit
    """)

def menu_manager():
    print("""
        1. Register Product
        2. Manage Stock 
        0. Exit
    """)

def main():
    con = sqlite3.connect(ROOT_PATH / 'supermarket_db.sqlite')
    try:
        while True:
            choice = int(input("1. Cashier\n2.Manager\n0. Exit\n"))

            if choice == 1:
                menu_checkout()
                op = int(input("? "))
                if op == 1:
                    code_bar = int(input("Code bar: "))
                    cpf = input("CPF: ")
                    sale = SalesManager(con)
                    sale.begin_sales(code_bar,cpf)
                elif op == 2:
                    customer = CustomerManager(con)
                    cpf = input("CPF: ")
                    name = input("Name: ")
                    birthday = input("Birthday: ")
                    address = input("Address: ")
                    phone_number = input("Phone number: ")
                    customer.add_customer(cpf, name, birthday, address, phone_number)
                else:
                    print("Invalid option!")
            elif choice == 2:
                menu_manager()
                op = int(input("? "))
                if op == 1:
                    product = ProductManager(con)
                    name = input("Product name: ")
                    brand = input("Brand: ")
                    expiration_date = input("Expiration date: ")
                    department = input("Department: ")
                    price = float(input("Price: "))
                    code_bar = int(input("Code bar: "))
                    product.add_product(name, brand, expiration_date, department, price, code_bar)
                elif op == 2:
                    pass
                else:
                    print("Invalid option!")
            elif op == 0:
                break
            else:
                print("Invalid option!")
    finally:
        con.close()

if __name__ == "__main__":
    main()