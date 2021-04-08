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
    print('\nCATEGORIAS:\n')
    count = 0
    for category in list_categories:
        count += 1
        items_category = category.split()
        print(f'Código: {count}\nNome: {items_category[0]}\nDescrição: {items_category[1]}\n')
