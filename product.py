from models import Product, Category
from settings import engine
from sqlalchemy.orm import sessionmaker
from category import filter_category, list_of_category


Session = sessionmaker(bind = engine)


def choosing_category():
    categories_list = []
    aux = True
    
    while aux:
        categories_list.append(int(input('Digite o código da categoria: ')))
        finish_choosing = input("Deseja incluir mais uma categoria? [s/n]")
        if finish_choosing == 'n' or finish_choosing == 'N':
            aux = False
    
    return categories_list


def create_product(name, description, value):
    '''
        User Story: Como usuário, eu quero criar um produto para tê-lo registrado.
        Desciption: Deve ler name, description, value, category; criar um produto e registrar no BD.
    '''

    list_of_category()

    categories_list = choosing_category()

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
        Desciption: Deve receber um projeto e salvar no BD.
    '''
    try:
        session = Session()
        all_products = session.query(Product).all()
        
        print('\nPRODUTOS:\n')
        _print_products(all_products)

    except:
        raise Exception("Erro, ao listar produtos")

    finally:
        session.close()


def _print_products(all_products):
    '''
        função "privada"
    '''
    for row in all_products:
        print ("Nome:",row.name, "; Descrição:",row.description, "; Preço:", row.value)
        _print_categories(row.categories)
        print("\n")


def _print_categories(categories):
    '''
        função "privada"
    '''
    count = 0
    for row_category in categories:
        count = count + 1
        print (f"Categoria {count}:", row_category.name)