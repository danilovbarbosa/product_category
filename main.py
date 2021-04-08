from os import path
import sys
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from category import *


def start():
    try:
        number = int(input(f"""
        -------------------------
        Selecione a opção deseja:
        -------------------------          
        1- Cadastrar categoria.
        2- Listas categorias.
        3- Cadastrar produto.
        4- Listar produtos.
        -------------------------
        Número: """))
        if number in range(1, 5):
            return number
        else:
            print('Opção não encontrada.')
            sys.exit()
    except Exception as e:
        print(e)


def get_function_for_number(number):
    if number == 1:
        create_category()
    elif number == 2:
        list_of_category()
    elif number == 3:
        return ''
    elif number == 4:
        return ''


def controller():
    get_function_for_number(start())


if __name__ == '__main__':
    controller()
