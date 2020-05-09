import psycopg2

def create():
    #connecting to psql
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='test123', port='5432')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE student(NAME TEXT, AGE INTEGER, ADDRESS TEXT);''')

    print('Table created.')
    conn.commit()
    conn.close()

def insert_data():
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='test123', port='5432')
    cursor = conn.cursor()

    name = input("Enter the name : ")
    age = int(input("Enter the age : "))
    address = input("Enter the address : ")
    query = '''INSERT INTO student (NAME, AGE, ADDRESS) VALUES (%s, %s, %s);'''
    cursor.execute(query, (name, age, address))

    print('Inserted.')
    conn.commit()
    conn.close()

insert_data()