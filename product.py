from models import Product, Category, engine
from sqlalchemy.orm import sessionmaker
from category import filter_category, list_of_category
Session = sessionmaker(bind = engine)


def create_product():
    '''
        User Story: Como usuário, eu quero criar um produto para tê-lo registrado.
        Desciption: Deve ler name, description, value, category; criar um produto e registrar no BD.
    '''

    categories_list = []
    name = input('Digite o nome do produto: ')
    description = input('Digite a descrição do produto: ')
    value = float(input('Digite o valor do produto R$ '))
    list_of_category()

    choosing_category = True
    while choosing_category:
        categories_list.append(int(input('Digite o código da categoria: ')))
        finish_choosing = input("Deseja incluir mais uma categoria? [s/n]")
        if finish_choosing == 'n' or finish_choosing == 'N':
                    choosing_category = False

    data_product(name, description, value, categories_list)


def data_product(name, description, value, categories_list):
    '''
        Desciption: Deve receber um projeto e salvar no BD.
    '''
    try:
        categories = []
        for id_category in categories_list:
            categories.append(filter_category(id_category))

        product_object = Product(name=name, value=value, description=description)
        product_object.categories.extend(categories)

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
        all_products = session.query.filter(Product.categories.any(id_category=category.id)).all()
        
        print('\nPRODUTOS:\n')

        for row in all_products:
            print ("Nome:",row.name, "Descrição:",row.description, "Preço:", row.price, "Categorias:", row.categories)

    except:
        raise Exception("Erro, ao listar produtos")

    finally:
        session.close()

if __name__ == '__main__':
    create_product()