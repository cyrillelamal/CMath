"""
Interface
"""
from FiniteConsole.FiniteConsole import Program, Menu, Option
from l5_elementary_functions import funcs as f


p = Program()
p.init_menu = Menu('main')
main = p.get_menu_by_id('main')
main.append_options(
    Option(1, 'first', 'Первая функция с логарифмом'),
    Option(2, 'second', 'Вторая функция с арктангенсом'),
    Option(9, 'exit', 'Выйти из программы')
)

Menu('first', f.logarithm)
Menu('second', f.arctan)

Menu('exit', lambda: exit())


def start():
    p.start_loop()
