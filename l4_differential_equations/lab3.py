from FiniteConsole import Program, Menu, Option
from l4_differential_equations import funcs as f


p = Program()
main = Menu('main')
p.init_menu = main

main.append_options(
    Option(1, 'euler', 'Метод Эйлера'),
    Option(2, 'rk', 'Метод Рунге-Кутта'),
    Option(3, 'double', 'ДУ 2 порядка'),
    Option(4, 'system', 'Система ДУ'),
    Option(5, 'exit', 'Выйти')
)

Menu('euler', f.euler)
Menu('rk', f.rk)
Menu('double', f.double)
Menu('system', f.system)
Menu('exit', lambda: exit())


def start():
    p.start_loop()
