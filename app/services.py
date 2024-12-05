from .models import Product
from .extensions import db

def get_all_products():
    #Obtiene todos los productos de la base de datos.
    return Product.query.all()

def get_product_by_id(product_id):
    #Obtiene un producto por su ID.
    return Product.query.get(product_id)

def create_product(data):
    #Crea un nuevo producto en la base de datos.
    new_product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        stock=data.get('stock', 0)
    )
    db.session.add(new_product)
    db.session.commit()
    return new_product

def update_product(product_id, data):
    #Actualiza un producto existente.
    product = Product.query.get(product_id)
    if not product:
        return None

    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.stock = data.get('stock', product.stock)

    db.session.commit()
    return product

def delete_product(product_id):
    #Elimina un producto por su ID.
    product = Product.query.get(product_id)
    if not product:
        return None

    db.session.delete(product)
    db.session.commit()
    return product
