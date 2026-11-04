
from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import date

from blueprint_app.app import db
from blueprint_app.pedidos.models import Pedido
from blueprint_app.clientes.models import Cliente
from blueprint_app.productos.models import Producto


bp_pedidos = Blueprint(
    'bp_pedidos',
    __name__,
    template_folder='templates'
)


# LISTAR PEDIDOS
@bp_pedidos.route('/')
def index():
    pedidos = Pedido.query.all()
    return render_template('pedidos/index.html', pedidos=pedidos)


# REGISTRAR PEDIDO
@bp_pedidos.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        pedido = Pedido(
            fecha=date.fromisoformat(request.form['fecha']),
            monto=float(request.form['monto']),
            producto_id=int(request.form['producto_id']),
            cliente_id=int(request.form['cliente_id'])
        )

        db.session.add(pedido)
        db.session.commit()

        flash('Pedido registrado correctamente', 'success')
        return redirect(url_for('bp_pedidos.index'))

    clientes = Cliente.query.all()
    productos = Producto.query.all()

    return render_template(
        'pedidos/nuevo.html',
        clientes=clientes,
        productos=productos
    )


# EDITAR PEDIDO
@bp_pedidos.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    pedido = Pedido.query.get_or_404(id)

    if request.method == 'POST':
        pedido.fecha = date.fromisoformat(request.form['fecha'])
        pedido.monto = float(request.form['monto'])
        pedido.producto_id = int(request.form['producto_id'])
        pedido.cliente_id = int(request.form['cliente_id'])

        db.session.commit()

        flash('Pedido actualizado correctamente', 'success')
        return redirect(url_for('bp_pedidos.index'))

    clientes = Cliente.query.all()
    productos = Producto.query.all()

    return render_template(
        'pedidos/editar.html',
        pedido=pedido,
        clientes=clientes,
        productos=productos
    )


# ELIMINAR PEDIDO
@bp_pedidos.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    pedido = Pedido.query.get_or_404(id)

    db.session.delete(pedido)
    db.session.commit()

    flash('Pedido eliminado correctamente', 'success')
    return redirect(url_for('bp_pedidos.index'))
