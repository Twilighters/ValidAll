from json.decoder import JSONDecodeError
import logging
import json

log = logging.getLogger(__name__)

class InputError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
    def __str__(self):
        return f'ошибка: {self.message}'

class MoveError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
    def __str__(self):
        return f'ошибка : {self.message}'

def check_move(matrix, move):
    return True

def check_input(move):
    return False

def checkmoving(_input):
    try:
        matrix = 0
        Command = json.loads(_input)
        if not check_input(Command):
            raise InputError("сработала ошибка")
        if not check_move(matrix, Command):
            raise MoveError("сработала вторая ошибка")
    except JSONDecodeError as err:
        log.error("Ошибка импорта")
    except InputError as err:
        log.error(f"Ошибка ввода {err}")
    except MoveError as err:
        log.error("Предел карты превышен")

checkmoving("{}")