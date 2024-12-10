## <summary>
# классы сущностей, необходимые для архитектуры базы данных в соответствии с ER-диаграммой
# ## </summary>

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from .config import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    registration_date = Column(DateTime)
    address = Column(String)
    phone = Column(String)

    reviews = relationship("Review", back_populates="user")
    orders = relationship("Order", back_populates="user")
    cart = relationship("Cart", back_populates="user")
    delivery_addresses = relationship("DeliveryAddress", back_populates="user")

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    article = Column(String, unique=True, index=True)
    price = Column(Float)
    stock_quantity = Column(Integer)
    description = Column(Text)
    main_photo = Column(String)
    additional_photos = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    subcategory_id = Column(Integer, ForeignKey('subcategories.id'))
    discount = Column(Float)
    hit_sales = Column(Boolean, default=False)
    new_arrival = Column(Boolean, default=False)
    promotion_id = Column(Integer, ForeignKey('promotions.id'))

    category = relationship("Category", back_populates="products")
    subcategory = relationship("Subcategory", back_populates="products")
    reviews = relationship("Review", back_populates="product")
    order_products = relationship("OrderProduct", back_populates="product")
    cart_items = relationship("CartItem", back_populates="product")

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)

    products = relationship("Product", back_populates="category")
    subcategories = relationship("Subcategory", back_populates="category")

class Subcategory(Base):
    __tablename__ = 'subcategories'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("Category", back_populates="subcategories")
    products = relationship("Product", back_populates="subcategory")

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    order_date = Column(DateTime)
    order_status = Column(String)
    payment_method_id = Column(Integer, ForeignKey('payment_methods.id'))
    delivery_method_id = Column(Integer, ForeignKey('delivery_methods.id'))

    user = relationship("User", back_populates="orders")
    order_products = relationship("OrderProduct", back_populates="order")
    order_history = relationship("OrderHistory", back_populates="order")
    payment = relationship("Payment", back_populates="order")

class PaymentMethod(Base):
    __tablename__ = 'payment_methods'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)

    orders = relationship("Order", back_populates="payment_method")
    payments = relationship("Payment", back_populates="payment_method")

class DeliveryMethod(Base):
    __tablename__ = 'delivery_methods'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)

    orders = relationship("Order", back_populates="delivery_method")

class Cart(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="cart")
    cart_items = relationship("CartItem", back_populates="cart")

class CartItem(Base):
    __tablename__ = 'cart_items'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey('carts.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)

    cart = relationship("Cart", back_populates="cart_items")
    product = relationship("Product", back_populates="cart_items")

class OrderProduct(Base):
    __tablename__ = 'order_products'
    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    quantity = Column(Integer)
    price = Column(Float)

    order = relationship("Order", back_populates="order_products")
    product = relationship("Product", back_populates="order_products")

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    review_text = Column(Text)
    rating = Column(Integer)
    review_date = Column(DateTime)
    moderation_status = Column(Boolean, default=False)

    user = relationship("User", back_populates="reviews")
    product = relationship("Product", back_populates="reviews")

class Promotion(Base):
    __tablename__ = 'promotions'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(Text)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    products = relationship("Product", back_populates="promotion")

class OrderHistory(Base):
    __tablename__ = 'order_history'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    status_change_date = Column(DateTime)
    new_status = Column(String)

    order = relationship("Order", back_populates="order_history")

class DeliveryAddress(Base):
    __tablename__ = 'delivery_addresses'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    address = Column(String)
    city = Column(String)
    postal_code = Column(String)
    country = Column(String)

    user = relationship("User", back_populates="delivery_addresses")

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    payment_method_id = Column(Integer, ForeignKey('payment_methods.id'))
    amount = Column(Float)
    payment_date = Column(DateTime)
    payment_status = Column(String)

    order = relationship("Order", back_populates="payment")
    payment_method = relationship("PaymentMethod", back_populates="payments")