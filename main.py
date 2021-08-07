class InputParameterVerificationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'ошибка: {self.message}'


class ResultVerificationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'ошибка: {self.message}'

user_input1 = 12
user_input2 = 2
on_fail_repeat_times = 1

def input_validation(user_input1, user_input2):
    if isinstance(user_input1, int):
        return True
    if isinstance(user_input2, int):
        return True
    else:
        return False


def result_validation(check_difference):
    if check_difference >= 0:
    #     return True
    # else:
        return False

def default_behavior ():
    return None

def my_decorator(input_validation, on_fail_repeat_times, result_validation):
    def decoration(func):
        def wrapper(*args):
            if not input_validation(user_input1, user_input2):
                raise InputParameterVerificationError("Должны быть только цифры")
            print("то что происходит ДО вызова функции")
            for i in range(on_fail_repeat_times):
                result = func(*args)
                check_difference = result
            print("то что происходит ПОСЛЕ вызова функции")
            if not result_validation(check_difference):
                if on_fail_repeat_times < 3:
                    raise ResultVerificationError("Ошибка проверки результата")
            return result

        return wrapper

    return decoration


@my_decorator(input_validation, on_fail_repeat_times, result_validation)
def difference(user_input1, user_input2):
    result = user_input1 - user_input2
    print(user_input1, user_input2, "То что происходит ВО ВРЕМЯ исполнения функции")
    return result


difference(user_input1, user_input2)