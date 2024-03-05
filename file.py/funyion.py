import psycopg2

class book():
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price
        self.author = []
        self.category = []
        self.id = id


def get_books(cur):
        cur.execute("select * from books;")
        for i in cur.fetchall():
            print(i[1])

def get_book(cur, title):
        cur.execute('select * from books where title = %s', (title,))
        book = cur.fetchone()
        return book
            
def get_author(cur, fullname):
        cur.execute('select * from authors where fullname = %s', (fullname,))
        author = cur.fetchone()
        return author

def add_author(fullname, cur):
        date_born = input('Введите год рождение автора')
        date_death = input('Введите год смерти автора')
        biography = input('Введите биографию автора')
        cur.execute("insert into authors(fullname, date_born, date_death, biography) values (%s, %s, %s, %s)", (fullname, date_born, date_death, biography))
        author = get_author(cur, fullname)
        return author

def add_book(cur):
        title = input('Введите название книги - ')
        price = input('Введите цену книги - ')
        fullname = input('Введите ФИО автора')
        author = get_author(cur, fullname)
        if author == None:
            author = add_author()
        book = get_book(cur,title)
        cur.execute("insert into books(title, price) values (%s, %s)", (title, price))
        cur.execute("insert into book_author(book_id, author_id) values (%s, %s)", (book[0], author[0]))
        

conn = psycopg2.connect("dbname=postgres user=postgres password=1231")
cur = conn.cursor()

while True:
        print('1 - посмотреть все книги, 2 выйти, 3 добавить книгу')
        command = input('Введите комманду - ')
        if command == '1':
            get_books(cur)
        elif command == '2':
            print('Вы вышли из программы')
            break
        elif command == '3':
            add_book(cur)
            conn.commit()
            
cur.close()
conn.close()