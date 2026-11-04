
from flask import Blueprint, render_template, request, redirect, url_for, flash

from blueprint_app.app import db
from blueprint_app.clientes.models import Cliente


bp_clientes = Blueprint(
    'bp_clientes',
    __name__,
    template_folder='templates'
)


# LISTAR CLIENTES
@bp_clientes.route('/')
def index():
    clientes = Cliente.query.all()
    return render_template('clientes/index.html', clientes=clientes)


# REGISTRAR CLIENTE
@bp_clientes.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']

        cliente = Cliente(
            nombre=nombre,
            telefono=telefono
        )

        db.session.add(cliente)
        db.session.commit()

        flash('Cliente registrado correctamente', 'success')
        return redirect(url_for('bp_clientes.index'))

    return render_template('clientes/nuevo.html')


# EDITAR CLIENTE
@bp_clientes.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    cliente = Cliente.query.get_or_404(id)

    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        cliente.telefono = request.form['telefono']

        db.session.commit()

        flash('Cliente actualizado correctamente', 'success')
        return redirect(url_for('bp_clientes.index'))

    return render_template('clientes/editar.html', cliente=cliente)


# ELIMINAR CLIENTE
@bp_clientes.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    cliente = Cliente.query.get_or_404(id)

    db.session.delete(cliente)
    db.session.commit()

    flash('Cliente eliminado correctamente', 'success')
    return redirect(url_for('bp_clientes.index'))
