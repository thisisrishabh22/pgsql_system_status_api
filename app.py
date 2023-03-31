#!/usr/bin/python
import psycopg2
import os
from flask import Flask, jsonify, request

def connect():
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host=os.environ.get('PGSQL_HOST'), user=os.environ.get('PGSQL_USER'))

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            return conn

app = Flask(__name__)

app.db = connect()


@app.route('/', methods = ['GET'])
def home():
    return jsonify({'message': 'welcome to pgsql system status API'})

@app.route('/pg_sys_os_info', methods = ['GET'])
def pg_sys_os_info():
    curr = app.db.cursor()
    curr.execute("SELECT public.pg_sys_os_info();")
    result = curr.fetchone()
    return jsonify({'results': result})

@app.route('/pg_sys_cpu_info', methods = ['GET'])
def pg_sys_cpu_info():
    curr = app.db.cursor()
    curr.execute("SELECT public.pg_sys_cpu_info();")
    result = curr.fetchone()
    return jsonify({'results': result})

@app.route('/pg_sys_cpu_usage_info', methods = ['GET'])
def pg_sys_cpu_usage_info():
    curr = app.db.cursor()
    curr.execute("SELECT public.pg_sys_cpu_usage_info();")
    result = curr.fetchone()
    return jsonify({'results': result})

@app.route('/pg_sys_memory_info', methods = ['GET'])
def pg_sys_memory_info():
    curr = app.db.cursor()
    curr.execute("SELECT public.pg_sys_memory_info();")
    result = curr.fetchone()
    return jsonify({'results': result})



if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=4500)
