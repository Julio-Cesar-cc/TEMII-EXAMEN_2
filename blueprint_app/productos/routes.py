
from flask import Blueprint, render_template, request, redirect, url_for, flash

from blueprint_app.app import db
from blueprint_app.productos.models import Producto


bp_productos = Blueprint(
    'bp_productos',
    __name__,
    template_folder='templates'
)

@bp_productos.route('/')
def index():
    productos = Producto.query.all()
    return render_template('productos/index.html', productos=productos)


@bp_productos.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']

        producto = Producto(
            nombre=nombre,
            precio=float(precio),
            stock=int(stock)
        )

        db.session.add(producto)
        db.session.commit()
        flash('Producto registrado correctamente', 'success')
        return redirect(url_for('bp_productos.index'))

    return render_template('productos/nuevo.html')

@bp_productos.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    producto = Producto.query.get_or_404(id)

    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.precio = float(request.form['precio'])
        producto.stock = int(request.form['stock'])

        db.session.commit()

        flash('Producto actualizado correctamente', 'success')
        return redirect(url_for('bp_productos.index'))

    return render_template('productos/editar.html', producto=producto)


@bp_productos.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    producto = Producto.query.get_or_404(id)

    db.session.delete(producto)
    db.session.commit()

    flash('Producto eliminado correctamente', 'success')
    return redirect(url_for('bp_productos.index'))