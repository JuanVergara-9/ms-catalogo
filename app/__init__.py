from flask import Flask
from .extensions import cache, db, migrate
from .routes import catalogo_bp
from .models import Product

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    
    # Cargar configuración desde el archivo config.py
    app.config.from_object(config_class)
    
    # Configuración de Flask-Caching
    app.config['CACHE_TYPE'] = 'SimpleCache'  # Cambia según el backend que desees usar
    app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # Tiempo de expiración por defecto (en segundos)
    
    # Inicialización de extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    
    # Registro de blueprints
    app.register_blueprint(catalogo_bp, url_prefix='/api/catalogo')

    return app
