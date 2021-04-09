from category import list_of_category
from models import Product, Category, engine
from sqlalchemy.orm import sessionmaker


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

        Session = sessionmaker(bind = engine)
        session = Session()
        session.add(product_object)
        session.commit()

    except:
        session.rollback()
        raise Exception("Erro, ao registrar produto.")

    finally:
        session.close()

def filter_category(id_category):
    try:
        Session = sessionmaker(bind = engine)
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

def list_of_product():
    '''
        TODO: refatorar
    '''
    '''
        Desciption: Deve receber um projeto e salvar no BD.
    '''
    list_products = open('product.txt', 'r')
    
    print('\nPRODUTOS:\n')
    
    for product in list_products:
        items_product = product.split(',')
        print(f'Nome: {items_product[0]}\nDescrição: {items_product[1]}\n Valor: {items_product[2]}\nCódigo da categoria: {items_product[3]}')


if __name__ == '__main__':
    create_product()