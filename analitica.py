from math import factorial


def combinations(n, k):
    """Количество сочетаний C из n по k."""
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


def count_ways_1(n, m, k):
    """
    Рассчитать количество способов распределения n шариков по m урнам
    с учетом:
    n - количество шариков
    m - всего урн,
    k - пустых урн,
    """
    if k > m:
        return 0

    # Выбор k пустых урн
    empty_urns_combinations = combinations(m, k)
    if m - k >= n:
        bolls_combinations = combinations(m-k, n)
    else:
        bolls_combinations = combinations(n, m-k)
    # Общее количество способов
    result_combinations = empty_urns_combinations * bolls_combinations
    return result_combinations



if __name__ == "__main__":
    print('-----Запущен метод аналитики-----')
    n = 5  # Количество шариков
    m = 10  # Количество урн
    total_ways = total_distributions(m, n)
    if m >= n:
        k_min = m - n
    else:
        k_min = 0
    probabilities_1 = []
    for k in list(range(k_min, m)):
        combinations_1 = count_ways_1(n, m, k)
        probabilities_1.append(combinations_1/total_ways)
    print(f'Результат {sum(probabilities_1)}')