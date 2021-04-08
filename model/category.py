class Category:

    def create_category(self):
        name = input('Informe um nome para a sua categoria: ')
        description = input('Informe uma descrição para esta categoria: ')
        register_category = f'{name} {description}'
        self.data_category(register_category)

    def data_category(self, category_object):
        new_category = str(category_object) + '\n'
        data = open('categories.txt', 'a')
        data.write(new_category)
        print('ok')

    def list_of_category(self):
        list_categories = open('categories.txt', 'r')
        print('CATEGORIAS:\n')
        for category in list_categories:
            items_category = category.split()
            print(f'Nome: {items_category[0]}\nDescrição: {items_category[1]}\n')
