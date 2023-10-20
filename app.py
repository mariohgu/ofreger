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
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("SELECT * FROM usuario")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)


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


@app.put("/api/user/<id>")
def update_user(id):
    updating_user = request.get_json()
    nombres = updating_user["Nombres"]
    apellidos = updating_user["Apellidos"]
    # tipodocumento = updating_user["TipoDocumento"]
    # numdocumento = updating_user["NumDocumento"]
    # direccion = updating_user["Direccion"]
    # telefono = updating_user["Telefono"]
    # email = updating_user["Email"]
    # cargo = updating_user["Cargo"]
    # username = updating_user["Username"]
    # clave = Fernet(key).encrypt(bytes(updating_user["Clave"], "utf-8"))
    # condicion = updating_user["Condicion"]

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute(
        f"UPDATE usuario SET nombres = '{nombres}', apellidos = '{apellidos}' where id = {id} RETURNING *"
    )
    updated_user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if updated_user is None:
        return jsonify({"message": "user not found"}), 404

    return jsonify(updated_user)


@app.delete("/api/user/<id>")
def delete_user(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("DELETE FROM usuario WHERE id = %s RETURNING *", (id,))
    user_delete = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if user_delete is None:
        return jsonify({"message": "user not found"}), 404

    return jsonify(user_delete)


@app.get("/api/user/<id>")
def get_user_by_id(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("SELECT * FROM usuario WHERE id = %s", (id,))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user is None:
        return jsonify({"message": "user not found"}), 404

    return jsonify(user)


if __name__ == "__main__":
    app.run(debug=True)
