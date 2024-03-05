import psycopg2
from functions import add_product, add_supply, make_sale

conn = psycopg2.connect(
dbname="postgres",
user="postgres",
password="1231",
host="localhost"
)
cur = conn.cursor()


while True:
        print("1. Добавить товар")
        print("2. Добавить поставку")
        print("3. Зарегистрировать продажу")
        print("4. Выйти")
        
        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите название товара: ")
            description = input("Введите описание товара: ")
            price = int("Введите цену: ")
            quantity = int(input("Введите количество товара: "))
            add_product(name, description, price, quantity)
        elif choice == "2":
            product_id = int(input("Введите ID товара: "))
            supplier = input("Введите имя поставщика или название компании: ")
            quantity = int(input("Введите количество поставляемого товара: "))
            add_supply(product_id, supplier, quantity)
        elif choice == "3":
            product_id = int(input("Введите ID товара: "))
            customer = input("Введите имя покупателя: ")
            quantity = int(input("Введите количество проданного товара: "))
            make_sale(product_id,customer, quantity)
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")

cur.close()
conn.close()

