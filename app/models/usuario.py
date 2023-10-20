from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Sequence

db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, Sequence("usuario_id_seq"), primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    tipodocumento = db.Column(db.String(20), nullable=False)
    numdocumento = db.Column(db.String(20), unique=True, nullable=False)
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(50), unique=True, nullable=False)
    cargo = db.Column(db.String(30))
    username = db.Column(db.String(20), unique=True, nullable=False)
    clave = db.Column(db.Text, nullable=False)
    condicion = db.Column(db.Integer)
    fechacreacion = db.Column(db.DateTime, default=db.func.current_timestamp())

    # ... otros campos y relaciones ...

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    # ... otros métodos ...
    def editar(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def desactivar(self):
        self.condicion = 0
        db.session.commit()

    def activar(self):
        self.condicion = 1
        db.session.commit()

    @classmethod
    def mostrar(cls, idusuario):
        return cls.query.get(idusuario)

    # Relación con permisousuario
    permisos_usuario_rel = db.relationship(
        "PermisoUsuario", backref="usuario", lazy=True
    )

    @classmethod
    def listar(cls):
        return cls.query.all()

    @classmethod
    def listarMarcados(cls, idusuario):
        return PermisoUsuario.query.filter_by(idusuario=idusuario).all()

    @classmethod
    def verificar(cls, username, clave):
        return cls.query.filter_by(username=username, clave=clave, condicion=1).first()


class Permiso(db.Model):
    __tablename__ = "permiso"

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String)

    # Relación con permisousuario
    permisos_usuario = db.relationship("PermisoUsuario", backref="permiso", lazy=True)


class PermisoUsuario(db.Model):
    __tablename__ = "permisousuario"

    id = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    idpermiso = db.Column(db.Integer, db.ForeignKey("permiso.id"), nullable=False)

    # Relaciones
    usuario_rel = db.relationship("Usuario", back_populates="permisos_usuario_rel")
