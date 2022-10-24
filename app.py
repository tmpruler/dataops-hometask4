import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__,template_folder='templates')

def get_db_connection():
    user_password = open(os.environ['DB_PASSWORD_FILE'], 'r').read()
    conn = psycopg2.connect(host='postgres', dbname='flaskdb', user=os.environ['DB_USERNAME'], password=user_password)
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM test;')
    rez = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', items=rez)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5555)
