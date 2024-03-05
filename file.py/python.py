import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1231",
    host="localhost",
)
print("[INFO] ура вы подключились к базе данных")


cur = conn.cursor()

# Пример создания таблицы товаров
cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        quantity INTEGER NOT NULL
    )
""")
conn.commit()



# Закрытие соединения с базой данных
cur.close()
conn.close()
