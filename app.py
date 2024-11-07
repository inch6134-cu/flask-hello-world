from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Alex Chang in 3308!'

@app.route('/db_test')
def test():
    # INTERNAL 
    conn = psycopg2.connect("postgresql://flask_hello_world_db_user:dlmqZKPSo3masMFcKkwZwEmLO5mgFfUT@dpg-csm2b2jtq21c738b8vk0-a/flask_hello_world_db")
    # EXTERNAL
    # conn = psycopg2.connect("postgresql://flask_hello_world_db_user:dlmqZKPSo3masMFcKkwZwEmLO5mgFfUT@dpg-csm2b2jtq21c738b8vk0-a.oregon-postgres.render.com/flask_hello_world_db")
    conn.close()
    return "Database connection successful"

@app.route('/db_create')
def create():
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

@app.route('/db_insert')
def insert():
    # INTERNAL 
    conn = psycopg2.connect("postgresql://flask_hello_world_db_user:dlmqZKPSo3masMFcKkwZwEmLO5mgFfUT@dpg-csm2b2jtq21c738b8vk0-a/flask_hello_world_db")
    # EXTERNAL
    # conn = psycopg2.connect("postgresql://flask_hello_world_db_user:dlmqZKPSo3masMFcKkwZwEmLO5mgFfUT@dpg-csm2b2jtq21c738b8vk0-a.oregon-postgres.render.com/flask_hello_world_db")
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
    return "Basketball Table Populated"

@app.route('/db_select')
def select():
    # INTERNAL 
    conn = psycopg2.connect("postgresql://flask_hello_world_db_user:dlmqZKPSo3masMFcKkwZwEmLO5mgFfUT@dpg-csm2b2jtq21c738b8vk0-a/flask_hello_world_db")
    # EXTERNAL
    # conn = psycopg2.connect("postgresql://flask_hello_world_db_user:dlmqZKPSo3masMFcKkwZwEmLO5mgFfUT@dpg-csm2b2jtq21c738b8vk0-a.oregon-postgres.render.com/flask_hello_world_db")
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    return response_string

@app.route('/db_drop')
def drop():
    # INTERNAL 
    conn = psycopg2.connect("postgresql://flask_hello_world_db_user:dlmqZKPSo3masMFcKkwZwEmLO5mgFfUT@dpg-csm2b2jtq21c738b8vk0-a/flask_hello_world_db")
    # EXTERNAL
    # conn = psycopg2.connect("postgresql://flask_hello_world_db_user:dlmqZKPSo3masMFcKkwZwEmLO5mgFfUT@dpg-csm2b2jtq21c738b8vk0-a.oregon-postgres.render.com/flask_hello_world_db")
    cur = conn.cursor()
    cur.execute('''
    DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table successfully dropped"
