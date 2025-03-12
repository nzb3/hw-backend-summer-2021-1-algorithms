__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    """Определяет отношение суммы четных элементов списка
    к сумме нечетных.

    Example:
        >> even_odd([1, 2, 3, 4, 5])
        0.6667
    """

    even_sum = sum(x for x in numbers if x % 2 == 0)
    odd_sum = sum(x for x in numbers if x % 2 != 0)

    try:
        return float(even_sum) / float(odd_sum)
    except ZeroDivisionError:
        return 0

