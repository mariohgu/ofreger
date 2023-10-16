from flask import Flask
from psycopg2 import connect


app = Flask(__name__)

host = 'localhost'
port = 5432
dbname = 'ofreger'
user = 'admin'
password = 'admin'

def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn

@app.get('/api/user')
def get_user():
    return 'obteniendo lista de usuarios'

@app.post('/api/user')
def create_user():
    return 'creando usuario'

@app.put('/api/user/1')
def update_user():
    return 'actualizando usuario 1'

@app.delete('/api/user/1')
def delete_user():
    return 'eliminando usuario 1'

@app.get('/api/user/1')
def get_user_by_id():
    return 'obteniendo usuario por id 1'


if __name__ == '__main__':
    app.run(debug=True)