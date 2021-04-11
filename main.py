from os import path
import sys
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from category import *
from product import *

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


def show_menu():
    print('''
    Selecione a opção deseja: 
    ------------------------- 
    1- Cadastrar categoria.
    2- Atualizar categoria.
    3- Listas categorias.
    4- Cadastrar produto.
    5- Listar produtos.
    0- Sair do programa.   
    -------------------------  
    ''')


def get_choice():
    show_menu()
    choice = int(input("Digite o seu número: "))
    return choice


def start():
    try:
        number = get_choice()
        if number in range(1, 6):
            return number

        elif number == 0:
            print('Encerrando a execução.')
            sys.exit()

        else:
            print('Opção não encontrada.')

    except Exception as e:
        print(e)


def get_function_for_number(number):
    if number == 1:
        name = input('Informe um nome para a sua categoria: ')
        description = input('Informe uma descrição para esta categoria: ')
        create_category(name, description)

    elif number == 2:
        list_of_category()
        id_category = input('Informe o id para a sua categoria: ')
        object_category = filter_category(id_category)

        if filter_category(id_category) != None:
            print(f"Nome: {object_category.name} e descrição: {object_category.description}")

            # name = input('Informe o novo nome para a sua categoria: ')
            # description = input('Informe uma nova descrição para esta categoria: ')
            # update_category(object_category, name, description)
        else:
            raise Exception("Erro, id não registrado.")

    elif number == 3:
        list_of_category()

    elif number == 4:
        name = input('Digite o nome do produto: ')
        description = input('Digite a descrição do produto: ')
        value = float(input('Digite o valor do produto R$ '))
        create_product(name, description, value)

    elif number == 5:
        list_of_product()


def controller():
    while True:
        get_function_for_number(start())


if __name__ == '__main__':
    controller()
