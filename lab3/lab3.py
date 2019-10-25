from FiniteConsole.FiniteConsole import Program, Menu, Option
from lab3 import funcs as f


p = Program()
main = Menu('main')
p.init_menu = main

main.append_options(
    Option(1, 'euler', 'Метод Эйлера'),
    Option(2, 'runge', 'Метод Рунге-Кутта'),
    Option(3, 'exit', 'Выйти')
)

Menu('euler', f.euler)
Menu('runge', f.runge)
Menu('exit', lambda: exit())


def start():
    p.start_loop()
