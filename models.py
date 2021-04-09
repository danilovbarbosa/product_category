from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Float
engine = create_engine('sqlite:///shop.db', echo = False)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import relationship


class CategoryProduct(Base):
    __tablename__ = 'category_product'

    id_category = Column(Integer, ForeignKey('category.id'), primary_key = True)
    id_product = Column(Integer, ForeignKey('product.id'), primary_key = True)


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    description = Column(String)

    def __str__():
        print(name)


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    value = Column(Float)
    description = Column(String)
    categories = relationship('Category', secondary = 'category_product')

    def __str__():
        print(name)

Base.metadata.create_all(engine)
