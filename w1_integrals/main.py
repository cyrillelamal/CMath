import sys

from FiniteConsole.FiniteConsole import Program, Menu, Option
import funcs as f

p = Program()
p.init_menu = Menu('main')
p.init_menu.append_options(
    Option(1, 'const_step', 'Методы с постоянным шагом.'),
    Option(2, 'var_step', 'Методы с переменным шагом.'),
    Option(3, 'exit', 'Выйти из программы.')
)

# Const steps
Menu('const_step').append_options(
    Option('1', 'left_t', 'Метод левых прямоугольников'),
    Option('2', 'right_t', 'Метод правых прямоугольников'),
    Option('3', 'trap', 'Метод трапеций'),
    Option('4', 'parabola', 'Метод парабол'),
    Option('5', 'main', 'В главное меню')
)
# Var steps
Menu('var_step').append_options(
    Option('1', 'alg_1', 'Алгоритм 1'),
    Option('2', 'alg_2', 'Алгоритм 2'),
    Option('3', 'main', 'В главное меню')
)

# Finite states
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


if __name__ == '__main__':
    p.start_loop()
