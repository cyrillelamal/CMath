import sys

from FiniteConsole.FiniteConsole import Menu, Option, Program
from l2_numeric_integration import funcs as f


p = Program()  # Program object
main = Menu('main')
p.init_menu = main

# Main 0
main.append_options(
    Option(1, 'u_int', 'Неопределенные интегралы'),
    Option(2, 'm_int', 'Кратные интегралы'),
    Option(3, 'exit', 'Выйти из программы')
)

# Undefined 1
Menu('u_int').append_options(
    Option(1, 'const_step', 'Методы с постоянным шагом'),
    Option(2, 'var_step', 'Методы с переменным шагом'),
    Option(3, 'main', 'Назад')
)

# Multiple 1
Menu('m_int').append_options(
    Option(1, 'double_int', 'Посчитать двойной интеграл'),  # Finite state
    Option(2, 'main', 'В главное меню')
)

# Const steps 2
Menu('const_step').append_options(
    Option('1', 'left_t', 'Метод левых прямоугольников'),
    Option('2', 'right_t', 'Метод правых прямоугольников'),
    Option('3', 'trap', 'Метод трапеций'),
    Option('4', 'parabola', 'Метод парабол'),
    Option('5', 'u_int', 'Назад')
)
# Var steps 2
Menu('var_step').append_options(
    Option('1', 'alg_1', 'Алгоритм 1'),
    Option('2', 'alg_2', 'Алгоритм 2'),
    Option('3', 'main', 'В главное меню')
)


# Finite states 3
# Exit
Menu('exit', lambda: sys.exit())
# Const steps
Menu('left_t', f.left_rectangles)
Menu('right_t', f.right_rectangles)
Menu('trap', f.trapezium)
Menu('parabola', f.parable)
# Var steps
Menu('alg_1', f.alg1)
Menu('alg_2', f.alg2)
# Double integral
Menu('double_int', f.double_int)


def start():
    p.start_loop()
