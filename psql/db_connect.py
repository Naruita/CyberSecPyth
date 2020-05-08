import psycopg2

#connecting to psql
conn = psycopg2.connect(dbname='postgres', user='postgres', password='test123', port='5432')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE student(NAME TEXT, AGE INTEGER, ADDRESS TEXT);''')

print('Table created.')
conn.commit()
conn.close()
