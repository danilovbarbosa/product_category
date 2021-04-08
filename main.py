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
        1- Cadastrar produto.
        2- Cadastrar categoria.
        3- Listar produtos.
        4- Listar categorias.
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
        return ''
    elif number == 2:
        return ''
    elif number == 3:
        create_category()
    elif number == 4:
        list_of_category()
    return ''


def controller():
    get_function_for_number(start())


if __name__ == '__main__':
    controller()
