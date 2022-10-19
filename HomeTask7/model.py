import controller
import view
import equation

first = 0
second = 0
ops = ''
total = 0

def init_first():
    global first
    first = controller.input_integer_or_equ('Введите выражение или число: ')

def init_second():
    global second
    second = controller.input_integer('Введите число: ')

def init_ops():
    global ops
    global first
    global total
    try:
        if '-' in first or '+' in first or '*' in first or '/' in first:
            ops = '='
            total = equation.calc_equ(first)
    except:
        ops = controller.input_operation('Введите операцию: ')
    if ops == '=':
        view.print_total()
        return True
    