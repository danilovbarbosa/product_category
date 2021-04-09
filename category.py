from models import Category
from sqlalchemy import create_engine
engine = create_engine('sqlite:///shop.db', echo = True)
from sqlalchemy.orm import sessionmaker


def create_category():
    name = input('Informe um nome para a sua categoria: ')
    description = input('Informe uma descrição para esta categoria: ')
    new_category = Category(name = name, description = description)
    Session = sessionmaker(bind = engine)
    session = Session()
    session.add(new_category)
    session.commit()


def data_category(category_object):
    new_category = str(category_object) + '\n'
    data = open('categories.txt', 'a')
    data.write(new_category)
    print('ok')


def list_of_category():
    print('\nCATEGORIAS:\n')
    Session = sessionmaker(bind = engine)
    session = Session()
    all_categories = session.query(Category).all()
    for row in all_categories:
        print ("Nome:",row.name, "Descrição:",row.description)
