from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Alex Chang in 3308!'

@app.route('/db_test')
def db_test():
    # INTERNAL 
    conn = psycopg2.connect("postgresql://flask_hello_world_db_user:dlmqZKPSo3masMFcKkwZwEmLO5mgFfUT@dpg-csm2b2jtq21c738b8vk0-a/flask_hello_world_db")
    # EXTERNAL
    # conn = psycopg2.connect("postgresql://flask_hello_world_db_user:dlmqZKPSo3masMFcKkwZwEmLO5mgFfUT@dpg-csm2b2jtq21c738b8vk0-a.oregon-postgres.render.com/flask_hello_world_db")
    conn.close()
    return "Database connection successful"

@app.route('/db_create')
def db_create():
    # INTERNAL 
    conn = psycopg2.connect("postgresql://flask_hello_world_db_user:dlmqZKPSo3masMFcKkwZwEmLO5mgFfUT@dpg-csm2b2jtq21c738b8vk0-a/flask_hello_world_db")
    # EXTERNAL
    # conn = psycopg2.connect("postgresql://flask_hello_world_db_user:dlmqZKPSo3masMFcKkwZwEmLO5mgFfUT@dpg-csm2b2jtq21c738b8vk0-a.oregon-postgres.render.com/flask_hello_world_db")
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
