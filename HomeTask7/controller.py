import logger
import model
import view


def input_integer(enter):
    while True:
        try:
            a = int(input(enter))
            return a
        except:
            view.error_value()

def input_integer_or_equ(enter):
    while True:
        b = input(enter)
        try:
            a = int(b)
            return a
        except:
            if '-' in str(b) or '+' in str(b) or '*' in str(b) or '/' in str(b):
                return b
            view.error_value()

def input_operation(enter):
    while True:
        a = input(enter)
        if a in ['+', '-', '*', '/', '=']:
            return a
        else:
            view.error_value()

def operation():
    match (model.ops):
        case '+':
            model.total = model.first + model.second
        case '-':
            model.total = model.first - model.second
        case '*':
            model.total = model.first * model.second
        case '/':
            while model.second == 0:
                print('На ноль делить нельзя!')
                model.init_second()
            model.total = int(model.first / model.second)

        case _:
            view.error_value()
    logger.logger(f'{model.first} {model.ops} {model.second} = {model.total}')