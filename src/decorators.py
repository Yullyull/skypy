import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable], Callable]:
    """Декоратор для логирования вызова функции.

    Логирует имя функции, результат успешного выполнения или
    тип ошибки и входные параметры при возникновении исключения.

    Args:
        filename: Путь к файлу для записи логов.
                  Если None — лог выводится в консоль.

    Returns:
        Декоратор, оборачивающий функцию.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                msg = f"{func.__name__} ok"
            except Exception as e:
                err_type = type(e).__name__
                msg = (
                    f"{func.__name__} error: {err_type}. "
                    f"Inputs: {args}, {kwargs}"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(msg + "\n")
                else:
                    print(msg)
                raise

            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(msg + "\n")
            else:
                print(msg)
            return result

        return wrapper

    return decorator
