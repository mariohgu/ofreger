from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.models.usuario import db
from app.views.usuario_views import usuario_bp

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost:5432/ofreger'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la extensión SQLAlchemy
db.init_app(app)

# Registrar el Blueprint
app.register_blueprint(usuario_bp)

# @usuario_bp.route('/usuario')
# def usuario():
#     return render_template('usuarios/usuario.html')

if __name__ == '__main__':
    app.run(debug=True)
