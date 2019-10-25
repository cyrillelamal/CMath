from FiniteConsole.FiniteConsole import Program, Option, Menu
from lab2 import funcs as f


p = Program()
p.init_menu = Menu('main')
p.init_menu.append_options(
    Option('1', 'newton', 'Метод Ньютона'),
    Option('2', 'chord', 'Метод хорд'),
    Option('3', 'dichotomy', 'Метод дихотомии'),
    Option('4', 'exit', 'Выйти из программы')
)

Menu('newton', f.newton)
Menu('chord', f.chord)
Menu('dichotomy', f.dichotomy)
Menu('exit', lambda: exit())


def start():
    p.start_loop()
