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
    return count_ways_k(m, n, k) * count_ways_k(m-k, n-(m-k), l)


def calculate_range_k_l(urns_number, balls_numbers):
    if urns_number >= balls_numbers:
        empty_urns_min = urns_number - balls_numbers
    else:
        empty_urns_min = 0
    k_range = list(range(empty_urns_min, urns_number-1))
    return k_range


def calculate_k_probs(urns_number, balls_numbers):
    total_ways = total_distributions(urns_number, balls_numbers)
    k_range = calculate_range_k_l(urns_number, balls_numbers)
    probs_k = []
    for k in k_range:
        combinations = count_ways_k(urns_number, balls_numbers, k)
        probs_k.append(combinations / total_ways)
    return probs_k


def calculate_l_probs(urns_number, balls_number):
    k_range = calculate_range_k_l(urns_number, balls_number)
    probs_kl = []
    for i in range(len(k_range)):
        probs_l = []
        total_ways = total_distributions(
            urns_number,
            balls_number
        ) * total_distributions(
            urns_number-k_range[i],
            balls_number-(urns_number-k_range[i])
        )
        l_range = calculate_range_k_l(urns_number-k_range[i], balls_number)
        for l in l_range:
            combinations = count_ways_l(urns_number, balls_number, k_range[i], l)
            probs_l.append(combinations / total_ways)
        probs_kl.append(probs_l)
    return probs_kl




if __name__ == "__main__":
    print('-----Запущен метод аналитики-----')
    # urns_numbers = list(range(1, 10))  # Количество урн
    urns_numbers = (10,)
    # balls_number = list(range(0, 10)) # Количество шариков
    balls_numbers = 5
    for urns_number in urns_numbers:
        print('--------------------------------------------------------')
        print(f'Результаты для {urns_number} урн и {balls_numbers} шариков')
        probs_k = calculate_k_probs(urns_number, balls_numbers)
        print(f'Вероятности для разных k: {probs_k}')
        print(f'Математическое ожидание вероятностей: {np.mean(probs_k)}')