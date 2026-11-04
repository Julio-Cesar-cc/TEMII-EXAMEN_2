
from blueprint_app.app import db


class Cliente(db.Model):

    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)

    # Relación: un cliente puede tener muchos pedidos
    pedidos = db.relationship('Pedido', backref='cliente', lazy=True)
