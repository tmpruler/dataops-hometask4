import os
import psycopg2

#conn = psycopg2.connect("host='postgres', database='flaskdb', user='test', password='qweqwe][p][p'")
conn = psycopg2.connect(host='postgres', dbname='flaskdb', user=os.environ['DB_USERNAME'], password=os.environ['DB_PASSWORD'])


# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS test;')
cur.execute('CREATE TABLE test (id serial PRIMARY KEY,'
                                 'string varchar (100) NOT NULL,'
                                 'number integer NOT NULL,'
                                 'rating integer NOT NULL,'
                                 'date date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO test (string, number, rating)'
            'VALUES (%s, %s, %s)',
            ('Архитектуры СОД', 4, 5)
            )
cur.execute('INSERT INTO test (string, number, rating)'
            'VALUES (%s, %s, %s)',
            ('Terraform', 1, 5)
            )
cur.execute('INSERT INTO test (string, number, rating)'
            'VALUES (%s, %s, %s)',
            ('Ansible', 2, 4)
            )
cur.execute('INSERT INTO test (string, number, rating)'
            'VALUES (%s, %s, %s)',
            ('Docker', 3, 0)
            )

conn.commit()

cur.close()
conn.close()
