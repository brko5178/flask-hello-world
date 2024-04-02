from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Brandon Kohrt in 3308'

@app.route('/db_test')
def test():
    conn = psycopg2.connect("postgres://lab10brko_user:IguC1w19ZFjTTNIUbd06hgxdQKkCnLLn@dpg-co644jv109ks73dnspmg-a/lab10brko")
    conn.close()
    return "Database connection successful"

@app.route('/db_create')
def create():
    conn = psycopg2.connect("postgres://lab10brko_user:IguC1w19ZFjTTNIUbd06hgxdQKkCnLLn@dpg-co644jv109ks73dnspmg-a/lab10brko")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball table successfully created"
                
@app.route('/db_insert')
def insert():
    conn = psycopg2.connect("postgres://lab10brko_user:IguC1w19ZFjTTNIUbd06hgxdQKkCnLLn@dpg-co644jv109ks73dnspmg-a/lab10brko")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball table successfully populated"

@app.route('/db_select')
def select():
    conn = psycopg2.connect("postgres://lab10brko_user:IguC1w19ZFjTTNIUbd06hgxdQKkCnLLn@dpg-co644jv109ks73dnspmg-a/lab10brko")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
        ''')
    table = curr.fetchall()
    conn.close()
    table_entry = ""
    table_entry += "<table>"
    for player in table:
        table_entry += "<tr>"
        for info in player:
            table_entry += "<td>{}</td>".format(info)
        table_entry += "</tr>"
    table_entry += "</table>"
    return table_entry

@app.route('/db_drop')
def select():
    conn = psycopg2.connect("postgres://lab10brko_user:IguC1w19ZFjTTNIUbd06hgxdQKkCnLLn@dpg-co644jv109ks73dnspmg-a/lab10brko")
    cur = conn.cursor()
    cur.execute('''
    DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return "Basketball table successfully dropped"
    

        