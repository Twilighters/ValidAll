import json
from typing import Any, Callable, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])


class InputParameterVerificationError(Exception):  # type: ignore
    """Создание класса ошибки проверки входных параметров."""

    def __init__(self, message: str):
        """Инициализация сообщения от родительского класса."""
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        """Переопределение строки в надпись об ошибке."""
        return f"ошибка: {self.message}"


class ResultVerificationError(Exception):  # type: ignore
    """Создание класса ошибки проверки результата выполнения функции."""

    def __init__(self, message: str):
        """Инициализация сообщения от родительского класса."""
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        """Переопределение строки в надпись об ошибке."""
        return f"ошибка: {self.message}"


with open("myJson.schema.json", "r", encoding="UTF-8") as file_json_schema:
    data_schema = json.load(file_json_schema)
with open("myJson.json", "r", encoding="UTF-8") as file_json:
    data = json.load(file_json)

from_json_input1 = data["Minuend"]
from_json_input2 = data["Subtrahend"]

user_input1 = int(from_json_input1)
user_input2 = int(from_json_input2)

on_fail_repeat_times = 1


def input_validation(user_input1: int, user_input2: int) -> bool:
    """Проверка инпутов на int."""
    if isinstance(user_input1, int) and isinstance(user_input2, int):
        return True
    else:
        return False


def result_validation(check_difference: int) -> bool:
    """Результат проверки валидации, где если check_difference больше нуля то возвращение True."""
    if check_difference >= 0:
        return True
    else:
        return False


def my_decorator(
    input_validation: Any, on_fail_repeat_times: Any, result_validation: Any
) -> F:
    """Функция для передачи параметров внутрь декоратора."""

    def decoration(func: F) -> F:
        """Декоратор определяющий внутри себя функцию 'обертку'."""

        def wrapper(*args: Any) -> F:
            """
            Функция, которая отрабатывает ДО и ПОСЛЕ вызова основной функции.

            Функция служит как 'обертка' для основной функции. В этой функции срабатывают основные функции валидации.
            """
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

        return cast(F, wrapper)

    return cast(F, decoration)


@my_decorator(input_validation, on_fail_repeat_times, result_validation)  # type: ignore
def difference(user_input1: int, user_input2: int) -> int:
    """Основная функция в которой в результате выполнения получается Разность между Уменьшаемым и Вычитаемым."""
    result = user_input1 - user_input2
    print(user_input1, user_input2, "То что происходит ВО ВРЕМЯ исполнения функции")
    return int(result)
