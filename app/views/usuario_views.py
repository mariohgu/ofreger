from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.usuario import db, Usuario

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/usuarios')
def listar_usuarios():
    usuarios = Usuario.listar()
    return render_template('usuarios/listar.html', usuarios=usuarios)

@usuario_bp.route('/usuario/<int:idusuario>')
def mostrar_usuario(idusuario):
    usuario = Usuario.mostrar(idusuario)
    if not usuario:
        flash('Usuario no encontrado', 'error')
        return redirect(url_for('usuario.listar_usuarios'))
    return render_template('usuarios/mostrar.html', usuario=usuario)

@usuario_bp.route('/usuario/editar/<int:idusuario>', methods=['GET', 'POST'])
def editar_usuario(idusuario):
    usuario = Usuario.mostrar(idusuario)
    if not usuario:
        flash('Usuario no encontrado', 'error')
        return redirect(url_for('usuario.listar_usuarios'))
    
    if request.method == 'POST':
        # Aquí, recogerías los datos del formulario y los usarías para actualizar el usuario.
        # Por ejemplo:
        usuario.editar(nombres=request.form['nombres'], apellidos=request.form['apellidos'])
        flash('Usuario actualizado con éxito', 'success')
        return redirect(url_for('usuario.mostrar_usuario', idusuario=idusuario))
    
    return render_template('usuarios/editar.html', usuario=usuario)

# ... otras rutas y controladores ...

    # ... (código previo en usuario_views.py) ...

@usuario_bp.route('/usuario/nuevo', methods=['GET', 'POST'])
def nuevo_usuario():
    if request.method == 'POST':
        # Aquí, recogerías los datos del formulario y los usarías para crear un nuevo usuario.
        nuevo_usuario = Usuario(
            nombres=request.form['nombres'],
            apellidos=request.form['apellidos'],
            # ... otros campos ...
        )
        nuevo_usuario.insertar()
        flash('Usuario creado con éxito', 'success')
        return redirect(url_for('usuario.listar_usuarios'))
    
    return render_template('usuarios/nuevo.html')

@usuario_bp.route('/usuario/desactivar/<int:idusuario>', methods=['POST'])
def desactivar_usuario(idusuario):
    usuario = Usuario.mostrar(idusuario)
    if not usuario:
        flash('Usuario no encontrado', 'error')
        return redirect(url_for('usuario.listar_usuarios'))
    usuario.desactivar()
    flash('Usuario desactivado con éxito', 'success')
    return redirect(url_for('usuario.listar_usuarios'))

@usuario_bp.route('/usuario/activar/<int:idusuario>', methods=['POST'])
def activar_usuario(idusuario):
    usuario = Usuario.mostrar(idusuario)
    if not usuario:
        flash('Usuario no encontrado', 'error')
        return redirect(url_for('usuario.listar_usuarios'))
    usuario.activar()
    flash('Usuario activado con éxito', 'success')
    return redirect(url_for('usuario.listar_usuarios'))

@usuario_bp.route('/usuario/verificar', methods=['POST'])
def verificar_usuario():
    username = request.form['username']
    clave = request.form['clave']
    usuario = Usuario.verificar(username, clave)
    if usuario:
        # Aquí, podrías iniciar sesión al usuario y redirigirlo a una página de inicio o dashboard.
        flash('Inicio de sesión exitoso', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Credenciales inválidas', 'error')
        return redirect(url_for('login'))
