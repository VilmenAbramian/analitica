import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def probs_random_urn(
        num_trials: int,
        num_balls: int,
        num_urns: int
) -> tuple[np.ndarray]:
    '''
    Вычисляет с помощью метода Монте-Карло вероятность того,
    что случайно выбранная урна окажется пустой, с 1м шариком,
    с 2мя и более шариками.
    :param num_trials: количество повторений симуляции
    :param num_balls: количество шариков
    :param num_urns: количество урн
    :return: кортеж со средними количествами урн
    с 1м, 2мя и 2+ шарикоми; а также
    вероятности из описания выше
    '''
    empty_counts = np.zeros(num_trials, dtype=int)
    one_ball_counts = np.zeros(num_trials, dtype=int)
    multiple_ball_counts = np.zeros(num_trials, dtype=int)
    urns = np.zeros(num_urns, dtype=int)

    for i in range(num_trials):
        urns.fill(0)

        urn_choices = np.random.randint(0, num_urns, size=num_balls)
        unique, counts = np.unique(urn_choices, return_counts=True)
        urns[unique] += counts

        empty_counts[i] = np.count_nonzero(urns == 0)
        one_ball_counts[i] = np.count_nonzero(urns == 1)
        multiple_ball_counts[i] = (
                num_urns - empty_counts[i] - one_ball_counts[i]
        )

    # Вычисляем средние значения
    avg_empty = np.mean(empty_counts)
    avg_one_ball = np.mean(one_ball_counts)
    avg_multiple_ball = np.mean(multiple_ball_counts)

    # Вероятности для случайно выбранной урны
    total_urn_counts = num_trials * num_urns  # Общее число наблюдений урн
    prob_empty = sum(empty_counts) / total_urn_counts
    prob_single = sum(one_ball_counts) / total_urn_counts
    prob_multi = sum(multiple_ball_counts) / total_urn_counts

    return (avg_empty, avg_one_ball, avg_multiple_ball,
            prob_empty, prob_single, prob_multi)


def probs_k_l(
        num_trials: int,
        num_balls: int,
        num_urns: int
) -> np.ndarray:
    """
    Оценивает вероятность, что в точности k урн будут пустыми
    и l урн будут содержать ровно один шар.

    :param num_trials: Число испытаний
    :param num_balls: Число шаров
    :param num_urns: Число урн
    :return: Матрица вероятностей P(k, l), где k - пустые урны, l - урны с 1 шаром.
    """
    results = np.zeros((num_urns + 1, num_urns + 1), dtype=float)  # Создаём матрицу (m+1)x(m+1)

    for _ in range(num_trials):
        urns = np.zeros(num_urns, dtype=int)  # Обнуляем урны перед каждым экспериментом

        # Заполняем урны случайными шарами
        urn_choices = np.random.randint(0, num_urns, size=num_balls)
        unique, counts = np.unique(urn_choices, return_counts=True)
        urns[unique] += counts

        # Считаем количество пустых и одношаровых урн
        k = np.count_nonzero(urns == 0)  # Пустые урны
        l = np.count_nonzero(urns == 1)  # Урны с одним шаром

        results[k, l] += 1  # Записываем в матрицу

    # Нормируем матрицу (делим на количество испытаний)
    results /= num_trials

    return results


if __name__ == '__main__':
    print('-----Запущен метод Монте-Карло-----')
    num_trials = 100_000  # Количество экспериментов
    num_balls = 45  # Количество шариков (RFID-меток)
    num_urns = 10  # Количество урн (слотов 2^Q)
    results = probs_k_l(num_trials, num_balls, num_urns)

    plt.figure(figsize=(8, 6))
    sns.heatmap(results, fmt=".3f", cmap="Blues", xticklabels=range(num_urns + 1),
                yticklabels=range(num_urns + 1))
    plt.xlabel("Количество урн с 1 шаром (l)")
    plt.ylabel("Количество пустых урн (k)")
    plt.title("Вероятности P(k, l)")
    plt.show()

    print("Результаты:")
    print(results)
