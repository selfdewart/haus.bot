import psycopg2
from datetime import date

conn = psycopg2.connect("dbname=postgres user=postgres password=1231")
cur = conn.cursor()
#

# Функция для добавления товара на склад
def add_product(name, description, price, quantity):
    cur.execute("INSERT INTO products (name, description, price, quantity) VALUES (%s, %s, %s, %s)", (name, description, price, quantity))
    conn.commit()

# Функция для добавления поставки товара
def add_supply(product_id, supplier, quantity):
    cur.execute("UPDATE products SET quantity = quantity + %s WHERE product_id = %s", (quantity, product_id))
    cur.execute("INSERT INTO supplies (product_id, supplier, quantity, supply_date) VALUES (%s, %s, %s, %s)", (product_id, supplier, quantity, date.today()))
    conn.commit()

# Функция для регистрации продажи товара
def make_sale(product_id, customer, quantity):
    cur.execute("UPDATE products SET quantity = quantity - %s WHERE product_id = %s", (quantity, product_id))
    cur.execute("INSERT INTO sales (product_id, customer, quantity, sale_date) VALUES (%s, %s, %s, %s)", (product_id, customer, quantity, date.today()))
    conn.commit()