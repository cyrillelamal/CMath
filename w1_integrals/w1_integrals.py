import sys

from FiniteConsole.FiniteConsole import Program, Menu, Option
import funcs as f


# Main menu1
main_menu = Menu('main')
main_menu.append_option(Option('1', 'const_step', 'Методы с постоянным шагом'))
main_menu.append_option(Option('2', 'var_step', 'Методы с переменным шагом'))
main_menu.append_option(Option('3', 'exit', 'Выйти из программы'))


# Exit (menu)
exit_menu = Menu('exit', lambda: sys.exit())


# Const steps menu
const_step_menu = Menu('const_step')
const_step_menu.append_option(Option('1', 'left_t', 'Метод левых прямоугольников'))
const_step_menu.append_option(Option('2', 'right_t', 'Метод правых прямоугольников'))
const_step_menu.append_option(Option('3', 'trap', 'Метод трапеций'))
const_step_menu.append_option(Option('4', 'parabola', 'Метод парабол'))
const_step_menu.append_option(Option('5', 'main', 'В глвное меню'))

left_t = Menu('left_t', f.left_triangles)  # Left triangles
right_t = Menu('right_t', f.right_triangles)  # Left triangles
trap = Menu('trap', f.trapezium)  # Trapezium
para = Menu('parabola', f.parable)  # Parable


# Var steps menu
var_step_menu = Menu('var_step')
var_step_menu.append_option(Option('1', 'alg_1', 'Алгоритм 1'))
var_step_menu.append_option(Option('2', 'alg_2', 'Алгоритм 2'))
var_step_menu.append_option(Option('3', 'main', 'В глвное меню'))

alg1 = Menu('alg_1', f.alg1)
alg2 = Menu('alg_2', f.alg2)


# PROGRAM
# MAIN
prog = Program(main_menu)
# EXIT
prog.append_menu(exit_menu)
# CONST
prog.append_menu(const_step_menu).append_menu(left_t).append_menu(right_t).append_menu(trap).append_menu(para)
# VAR
prog.append_menu(var_step_menu).append_menu(alg1).append_menu(alg2)


prog.loop()
