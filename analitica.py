from math import factorial

import numpy as np


def combinations(n, k):
    """
    Количество сочетаний C из n (обозначение снизу)
    по k (обозначение сверху)
    """
    if k > n or k < 0:
        raise ValueError('k must be >= n')
    return factorial(n) // (factorial(k) * factorial(n - k))


def total_distributions(m, n):
    """
    Вычислить общее количество всех возможных распределений.
    m - урны
    n - шарики
    """
    return m**n


def count_ways_k(m:int, n:int, k:int) -> int:
    """
    Расчёт количества способов распределить шарики по урнам
    таким образом, чтобы:
    - k урн были пустыми
    - m-k урн были не пустыми
    Параметры:
    m - всего урн,
    n - количество шариков,
    k - пустых урн.
    """
    if k > m:
        raise ValueError('k must be less than m')

    # Выбор k пустых урн
    empty_urns_combinations = combinations(m, k)
    if m - k >= n:
        bolls_combinations = combinations(m-k, n)
    else:
        bolls_combinations = combinations(n, m-k)
    # Общее количество способов
    result_combinations = empty_urns_combinations * bolls_combinations
    return result_combinations


def count_ways_l(m:int, n:int, k:int, l:int) -> int:
    """
    Расчёт количества способов распределить шарики по урнам
    таким образом, чтобы:
    - k урн были пустыми
    - l урн содержали 1 и только 1 шарик
    - m-k-l урн содержали 2 и более шариков
    Параметры:
    m - всего урн,
    n - количество шариков,
    k - количество пустых урн,
    l - количество урн с 1 шариком
    """
    return count_ways_k(m, n, k) * count_ways_k(l, n-(m-k), m-k)


def calculate_range_k(urns_number, balls_numbers):
    if urns_number >= balls_numbers:
        empty_urns_min = urns_number - balls_numbers
    else:
        empty_urns_min = 0
    k_range = list(range(empty_urns_min, urns_number-1))
    return k_range


def calculate_k_probs(urns_number, balls_numbers, k_range):
    total_ways_k = total_distributions(urns_number, balls_numbers)
    probs_k = []
    for k in k_range:
        combinations_1 = count_ways_k(urns_number, balls_numbers, k)
        probs_k.append(combinations_1 / total_ways_k)
    return probs_k

if __name__ == "__main__":
    print('-----Запущен метод аналитики-----')
    # urns_numbers = list(range(1, 10))  # Количество урн
    urns_numbers = (10,)
    # balls_numbers = list(range(0, 10)) # Количество шариков
    balls_numbers = 5
    for urns_number in urns_numbers:
        print('--------------------------------------------------------')
        print(f'Результаты для {urns_number} урн и {balls_numbers} шариков')

        k_range = calculate_range_k(urns_number, balls_numbers)
        probs_k = calculate_k_probs(urns_number, balls_numbers, k_range)
        print(f'Вероятности для k в диапазоне {k_range}: {probs_k}')
        print(f'Математическое ожидание вероятностей: {np.mean(probs_k)}')