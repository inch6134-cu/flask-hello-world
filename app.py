from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Alex Chang in 3308!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://flask_hello_world_db_user:dlmqZKPSo3masMFcKkwZwEmLO5mgFfUT@dpg-csm2b2jtq21c738b8vk0-a/flask_hello_world_db")
    conn.close()
    return "Database connection successful"
