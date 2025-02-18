import matplotlib.pyplot as plt
from math import factorial
import numpy as np
import seaborn as sns


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


def count_ways_k(m: int, n: int, k: int) -> int:
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
    ways_to_fill = m - k
    ball_distributions = total_distributions(ways_to_fill, n)
    return empty_urns_combinations * ball_distributions


def count_ways_l(m, n, k, l):
    """
    Число способов распределить шары так, чтобы:
    - k урн были пустыми
    - l урн содержали ровно 1 шар
    - m - k - l урн содержали 2+ шара
    """
    if k + l > m or k > m or l > m:
        return 0  # Невозможные случаи

    ways_to_choose_k = combinations(m, k)  # Выбираем пустые урны
    ways_to_choose_l = combinations(m - k, l)  # Выбираем урны с 1 шаром
    remaining_balls = n - l  # Оставшиеся шары (мы уже распределили l шаров)

    # Проверяем, есть ли урны для заполнения
    if m - k - l > 0:
        ways_to_fill_remaining = total_distributions(m - k - l, remaining_balls)
    else:
        ways_to_fill_remaining = 1 if remaining_balls == 0 else 0  # Если нет урн, но шары остались — ошибка

    return ways_to_choose_k * ways_to_choose_l * ways_to_fill_remaining


def calculate_range_k_l(urns_number, balls_numbers):
    if urns_number >= balls_numbers:
        empty_urns_min = urns_number - balls_numbers
    else:
        empty_urns_min = 0
    k_range = list(range(empty_urns_min, urns_number-1))
    return k_range


def analit_probs_k_l(m, n):
    """
    Вычисляет матрицу вероятностей P(k, l), аналогичную Монте-Карло методу.

    :param m: Количество урн
    :param n: Количество шаров
    :return: Матрица P(k, l), где k - пустые урны, l - урны с 1 шариком
    """
    total_ways = total_distributions(m, n)
    prob_matrix = np.zeros((m + 1, m + 1), dtype=float)

    for k in range(m + 1):
        for l in range(m - k + 1):  # l не может превышать m - k
            prob_matrix[k, l] = count_ways_l(m, n, k, l) / total_ways

    return prob_matrix


if __name__ == "__main__":
    print('-----Запущен метод аналитики-----')
    urns_number = 10
    balls_number = 5
    prob_matrix = analit_probs_k_l(urns_number, balls_number)

    plt.figure(figsize=(8, 6))
    sns.heatmap(prob_matrix, annot=False, fmt=".5f", cmap="Blues")
    plt.xlabel("Урны с 1 шаром (l)")
    plt.ylabel("Пустые урны (k)")
    plt.title("Аналитическая вероятность P(k, l)")
    plt.show()

    print("Аналитическая матрица вероятностей P(k, l):")
    print(prob_matrix)
