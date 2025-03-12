from typing import TypeVar

__all__ = (
    "flip_kv_vk",
    "flip_kv_vk_safe",
)


KT = TypeVar("KT")
KV = TypeVar("KV")


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    """Формирует словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - ключи.

    Example:
        >> flip_kv_vk({'tokyo': 'Токио', 'moscow': 'Москва'})
        {
            'Токио': 'tokyo',
            'Москва': 'moscow',
        }
    """
    return {value: key for key, value in d.items()}

def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    """Формирует словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - список ключей,
    конфликтующих значений.

    Example:
        >> flip_kv_vk({'Санкт-Петербург': '+3', 'Москва': '+3'})
        {
            '+3': ['Москва', 'Санкт-Петербург'],
        }
    """

    result: dict[KV, list[KT]] = {}
    for key, value in d.items():
        result.setdefault(value, []).append(key)
    return result
