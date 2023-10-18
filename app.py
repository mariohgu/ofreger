from flask import Flask, request, jsonify
from psycopg2 import connect, extras
from cryptography.fernet import Fernet


app = Flask(__name__)
key = Fernet.generate_key()

host = "localhost"
port = 5432
dbname = "ofreger"
user = "admin"
password = "admin"


def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn


@app.get("/api/user")
def get_user():
    return "obteniendo lista de usuarios"


@app.post("/api/user")
def create_user():
    new_user = request.get_json()

    nombres = new_user["Nombres"]
    apellidos = new_user["Apellidos"]
    tipodocumento = new_user["TipoDocumento"]
    numdocumento = new_user["NumDocumento"]
    direccion = new_user["Direccion"]
    telefono = new_user["Telefono"]
    email = new_user["Email"]
    cargo = new_user["Cargo"]
    username = new_user["Username"]
    clave = Fernet(key).encrypt(bytes(new_user["Clave"], "utf-8"))
    condicion = new_user["Condicion"]

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute(
        "INSERT INTO Usuario (Nombres, Apellidos, TipoDocumento, NumDocumento, Direccion, Telefono, Email, Cargo, Username, Clave, Condicion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *",
        (
            nombres,
            apellidos,
            tipodocumento,
            numdocumento,
            direccion,
            telefono,
            email,
            cargo,
            username,
            clave,
            condicion,
        ),
    )
    new_user_register = cur.fetchone()    

    conn.commit()
    cur.close()
    conn.close()
    return jsonify(new_user_register)


@app.put("/api/user/1")
def update_user():
    return "actualizando usuario 1"


@app.delete("/api/user/1")
def delete_user():
    return "eliminando usuario 1"


@app.get("/api/user/1")
def get_user_by_id():
    return "obteniendo usuario por id 1"


if __name__ == "__main__":
    app.run(debug=True)
