from category import list_of_category
from models import Product, Category, engine
from sqlalchemy.orm import sessionmaker
from category import filter_category
Session = sessionmaker(bind = engine)


def create_product():
    '''
        User Story: Como usuário, eu quero criar um produto para tê-lo registrado.
        Desciption: Deve ler name, description, value, category; criar um produto e registrar no BD.
    '''

    list_of_category()

    name = input('Digite o nome do produto: ')
    description = input('Digite a descrição do produto: ')
    value = float(input('Digite o valor do produto R$ '))
    id_category = int(input('Digite o código da categoria: '))

    data_product(name, description, value, id_category)


def data_product(name, description, value, id_category):
    '''
        Desciption: Deve receber um projeto e salvar no BD.
    '''
    try:
        category = filter_category(id_category)

        product_object = Product(name=name, value=value, description=description)
        product_object.categories.append(category)

        session = Session()
        session.add(product_object)
        session.commit()

    except:
        session.rollback()
        raise Exception("Erro, ao registrar produto.")

    finally:
        session.close()


def list_of_product():
    '''
        TODO: refatorar
    '''
    '''
        Desciption: Deve receber um projeto e salvar no BD.
    '''
    try:
        session = Session()
        all_products = session.query(Product).all()
        
        print('\nPRODUTOS:\n')

        for row in all_products:
            print ("Nome:",row.name, "Descrição:",row.description)

    except:
        raise Exception("Erro, ao listar produtos")

    finally:
        session.close()

if __name__ == '__main__':
    create_product()