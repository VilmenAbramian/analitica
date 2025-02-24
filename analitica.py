import math

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import comb, factorial


def count_prob(m, n, k, l):
    """Вероятность того, что:
    - k урн пустые
    - l урн содержат ровно 1 шар
    - (m - k - l) урн содержат 2+ шаров
    """
    p = 1/m
    q = (m - 1)/m
    if k + l == m:
        return comb(m, k) * math.pow(p, l) * math.pow(q, n*k+l*(n-1))
    elif (k +l < m) and (2*m - 2*k - l == n):
        return comb(m, k) * comb(m-k, l) * math.pow(p, l+2*(m-k-l)) * math.pow(q, n*k+l*(n-1)+(n-l-2)*(m-k-l))
    elif (k + l < m) and (2*m -2*k - l > n):
        return comb(m, k) * math.pow(q, n*k) * comb(m-k, l) * math.pow(p, l) * math.pow(q, l*(n-1)) * math.pow(1-math.pow(q, n-l)-p*math.pow(q,n-l-1), m-k-l)

    raise ValueError('Недопустимое значение!')


def analit_probs_k_l(m, n):
    """Заполнение матрицы вероятностей P(k, l)"""
    prob_matrix = np.zeros((m + 1, m + 1))

    for k in range(m + 1):
        for l in range(m - k + 1):  # l не может быть больше (m - k)
            prob_matrix[k, l] = count_prob(m, n, k, l)

    return prob_matrix


if __name__ == "__main__":
    urns_number = 10
    balls_number = 1

    prob_matrix = analit_probs_k_l(urns_number, balls_number)

    plt.figure(figsize=(8, 6))
    sns.heatmap(prob_matrix, annot=False, fmt=".5f", cmap="Blues")
    plt.xlabel("Урны с 1 шаром (l)")
    plt.ylabel("Пустые урны (k)")
    plt.title("Аналитическая вероятность P(k, l)")
    plt.show()

    print("Аналитическая матрица вероятностей P(k, l):")
    print(prob_matrix)