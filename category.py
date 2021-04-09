from models import Category
from sqlalchemy import create_engine
engine = create_engine('sqlite:///shop.db', echo = True)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)

def create_category():
    name = input('Informe um nome para a sua categoria: ')
    description = input('Informe uma descrição para esta categoria: ')
    new_category = Category(name = name, description = description)
    data_category(new_category)

def data_category(category):
    try:
        session = Session()
        session.add(category)
        session.commit()
    except:
        session.rollback()
        raise Exception("Erro, ao adicionar categoria")
    finally:
        session.close()



def list_of_category():
    try:
        session = Session()
        all_categories = session.query(Category).all()
        print('\nCATEGORIAS:\n')
        for row in all_categories:
            print ("Nome:",row.name, "Descrição:",row.description)
    except:
        raise Exception("Erro, ao listar categorias")
    finally:
        session.close()

