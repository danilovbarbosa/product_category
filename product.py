from category import list_of_category


def create_product():
    list_of_category()
    print()
    name = input('Digite o nome do produto: ')
    description = input('Digite a descrição do produto: ')
    value = float(input('Digite o valor do produto R$ '))
    category = int(input('Digite o código da categoria: '))
    register_product = f'{name},{description},{value},{category}'
    data_product(register_product)


def data_product(product_object):
    new_product = str(product_object) + '\n'
    data = open('product.txt', 'a')
    data.write(new_product)
    print('ok')


def list_of_product():
    list_products = open('product.txt', 'r')
    print('\nPRODUTOS:\n')
    for product in list_products:
        items_product = product.split(',')
        print(f'Nome: {items_product[0]}\nDescrição: {items_product[1]}\n Valor: {items_product[2]}\nCódigo da categoria: {items_product[3]}')
