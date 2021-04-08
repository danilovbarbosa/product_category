import json

"""
def create_category():
    name = input('Informe um nome para a sua categoria: ')
    description = input('Informe uma descrição para esta categoria: ')
    info_category = {
        "name": name,
        "description": description
    }
    data_category(info_category)


def data_category(category_object):
    new_category = str(category_object)
    data = open('categories.txt', 'a')
    data.writelines(new_category)
    print('ok')


def list_of_category():
    list_categories = open('categories.txt', 'r')
    for category in list_categories:
        category_json = json.loads(category)
        for item in category_json:
            print(item)
        # /print(category_json["name"])
        # name = category_json["name"]
        # print(name)
        # print(f'Categoria: {category_json[0]}\nDescrição: {category_json[1]}')


# create_category()
list_of_category()
"""


def create_category():
    name = input('Informe um nome para a sua categoria: ')
    description = input('Informe uma descrição para esta categoria: ')
    register_category = f'{name} {description}'
    data_category(register_category)


def data_category(category_object):
    new_category = str(category_object) + '\n'
    data = open('categories.txt', 'a')
    data.write(new_category)
    print('ok')


def list_of_category():
    list_categories = open('categories.txt', 'r')
    print('CATEGORIAS:\n')
    for category in list_categories:
        items_category = category.split()
        print(f'Nome: {items_category[0]}\nDescrição: {items_category[1]}\n')


# create_category()
list_of_category()