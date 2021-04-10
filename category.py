from models import Category
from sqlalchemy import create_engine
from settings import engine
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
            print ("ID:", row.id, "Nome:",row.name, "Descrição:",row.description)
    except:
        raise Exception("Erro, ao listar categorias")
    finally:
        session.close()


def filter_category(id_category):
    try:
        session = Session()
        result = session.query(Category).filter(Category.id==id_category)

        if (result.count()) == 1:
            category = result[0]
            session.close()
            return category

    except:
        session.rollback()
        raise Exception("Erro, ao filtrar categoria.")

    finally:
        session.close()
