
from blueprint_app.app import db


class Pedido(db.Model):

    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    monto = db.Column(db.Float, nullable=False)

    # Claves foráneas
    producto_id = db.Column(
        db.Integer,
        db.ForeignKey('productos.id'),
        nullable=False
    )

    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey('clientes.id'),
        nullable=False
    )

    # Relación con Producto
    producto = db.relationship('Producto', backref='pedidos')
