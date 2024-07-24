import sqlite3
from customer_manager import CustomerManager
from product_manager import ProductManager

def test_add_customer():
    con = sqlite3.connect('supermarket_db.sqlite')
    cursor = con.cursor()
    customers = [
        ('12345678900', 'Jonas Silva', '1990-01-01', '123 Main St', '1234567890'),
        ('09876543211', 'Carla Pereira', '1985-02-02', '456 Oak St', '0987654321'),
        ('11223344556', 'Alice Botelho', '1975-03-03', '789 Pine St', '1122334455'),
        ('66778899001', 'Barbara Soares', '1980-04-04', '321 Maple St', '6677889900'),
        ('22334455667', 'Carol Pereira', '1995-05-05', '654 Birch St', '2233445566'),
    ]
    try:
        cursor.executemany("INSERT INTO customers (cpf, name, birthday, address, phone_number) VALUES (?, ?, ?, ?, ?)", customers)
        con.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        con.close()

def test_add_product():
    con = sqlite3.connect('supermarket_db.sqlite')
    cursor = con.cursor()
    #(name, brand, expiration_date, department, price, code_bar)
    products = [
        ('Detroit-Style Pepperoni Pizza', 'Great Value', '2025-01-01', 'Frozen', 2.50, 100001),
        ('Dino Shaped Chicken Breast Nuggets', 'Great Value', '2025-02-01', 'Frozen', 5.97, 100002),
        ('Restaurant Style Rotisserie Seasoned Crispy Wings', 'Tyson Foods', '2025-03-01', 'Frozen', 8.47, 100003),
        ('Dipped Chocolate Ice Cream Bar', 'bettergoods', '2025-04-01', 'Frozen', 2.97, 100004),
        ('Pineapple Mango + Probiotics Smoothie Mix', 'bettergoods', '2025-05-01', 'Frozen', 3.12, 100005),
        ('Danish Nut Gourmet Cookie Tin', 'Little Dutch Boy Bakery', '2024-12-01', 'Bakery', 19.98, 200001),
        ('Homestyle Tortillas', 'La Banderita', '2024-11-01', 'Bakery', 2.50, 200002),
        ('Plain Bagels, 6 count, Soft Pre-sliced Bagels, 20 oz Bag', 'Thomas', '2024-10-01', 'Bakery', 3.76, 200003),
        ('Regular Cinnamon Rolls', 'Freshness Guaranteed', '2024-09-01', 'Bakery', 2.78, 200004),
        ('Honey Wheat Sandwich Bread Loaf, 20 oz', 'Natures Own', '2024-08-01', 'Bakery', 2.25, 200005),
        ('Coca-Cola Classic Soda Pop Fridge ', 'Coca-Cola', '2024-07-01', 'Beverages', 3.50, 300001),
        ('Gatorade Thirst Quencher', 'Gatorade', '2024-06-01', 'Beverages', 7.30, 300002),
        ('Sams Cola Soda, 2 Liter Bottle', 'Sams', '2024-05-01', 'Beverages', 0.40, 300003),
        ('Sprite Lemon Lime Soda', 'Sprite', '2024-04-01', 'Beverages', 0.60, 300004),
        ('Sports Hydration Drink', 'Great Value', '2024-03-01', 'Beverages', 6.70, 300005),
        (' Body Wash', 'Dove', '2024-02-01', 'Personal Care', 5.00, 400001),
        ('Lavender Oil', 'Dove', '2024-01-01', 'Personal Care', 1.00, 400002),
        ('Antiperspirant Deodorant Spray', 'Axe', '2024-12-01', 'Personal Care', 2.00, 400003),
        ('Hand Sanitizer', 'Germ-X', '2024-11-01', 'Personal Care', 5.50, 400004),
        ('Toothpaste', 'Colgate', '2024-10-01', 'Personal Care', 4.00, 400005),
    ]
    try:
        cursor.executemany("INSERT INTO products (name, brand, expiration_date, department, price, code_bar) VALUES (?, ?, ?, ?, ?, ?)", products)
        con.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        con.close()


test_add_customer()
test_add_product()