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