
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'techbol2026'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///techbol.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from blueprint_app.productos import models
    from blueprint_app.clientes import models
    from blueprint_app.pedidos import models

    # Registrar Blueprint principal
    from blueprint_app.core.routes import bp as core_bp
    app.register_blueprint(core_bp)

    from blueprint_app.productos.routes import bp_productos
    app.register_blueprint(bp_productos, url_prefix='/productos')

    from blueprint_app.clientes.routes import bp_clientes
    app.register_blueprint(bp_clientes, url_prefix='/clientes')

    from blueprint_app.pedidos.routes import bp_pedidos
    app.register_blueprint(bp_pedidos, url_prefix='/pedidos')

    

    return app
