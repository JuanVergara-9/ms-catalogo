import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:12345678@localhost:5432/catalogo_db?client_encoding=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuración de caching
    CACHE_TYPE = 'SimpleCache'  # Cambiar a 'RedisCache' si usas Redis
    CACHE_DEFAULT_TIMEOUT = 300  # Tiempo por defecto para el cache
