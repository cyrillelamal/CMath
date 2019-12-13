"""
Interface
"""
from FiniteConsole import Program, Menu, Option
from l5_elementary_functions import funcs as f


p = Program()
main = Menu('main')
p.init_menu = main
main.append_options(
    Option(1, 'first', 'Первая функция с логарифмом'),
    Option(2, 'second', 'Вторая функция с арктангенсом'),
    Option(3, 'first_cheb', 'Первая функция с логарифмом (Чебышев)'),
    Option(4, 'second_cheb', 'Вторая функция с арктангенсом (Чебышев)'),
    Option(9, 'exit', 'Выйти из программы')
)

Menu('first', f.logarithm)
Menu('second', f.arctan)
Menu('first_cheb', f.logarithm_cheb)
Menu('second_cheb', f.arctan_cheb)

Menu('exit', lambda: exit())


def start():
    p.start_loop()
