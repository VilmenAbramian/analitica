import numpy as np


def monte_carlo_simulation(num_trials, num_balls, num_urns):
    empty_counts = np.zeros(num_trials, dtype=int)
    one_ball_counts = np.zeros(num_trials, dtype=int)
    multiple_ball_counts = np.zeros(num_trials, dtype=int)
    urns = np.zeros(num_urns, dtype=int)

    for i in range(num_trials):
        urns.fill(0)

        urn_choices = np.random.randint(0, num_urns, size = num_balls)
        unique, counts = np.unique(urn_choices, return_counts=True)
        urns[unique] += counts

        empty_counts[i] = np.count_nonzero(urns == 0)
        one_ball_counts[i] = np.count_nonzero(urns == 1)
        multiple_ball_counts[i] = num_urns - empty_counts[i] - one_ball_counts[i]

    # Вычисляем средние значения
    avg_empty = np.mean(empty_counts)
    avg_one_ball = np.mean(one_ball_counts)
    avg_multiple_ball = np.mean(multiple_ball_counts)

    # Вероятности для случайно выбранной урны
    total_urn_counts = num_trials * num_urns  # Общее число наблюдений урн
    prob_empty = sum(empty_counts) / total_urn_counts
    prob_single = sum(one_ball_counts) / total_urn_counts
    prob_multi = sum(multiple_ball_counts) / total_urn_counts

    return avg_empty, avg_one_ball, avg_multiple_ball, prob_empty, prob_single, prob_multi


if __name__ == '__main__':
    print('-----Запущен метод Монте-Карло-----')
    num_trials = 1000 # Количество экспериментов
    num_balls = 5  # Количество шариков (RFID-меток)
    num_urns = 10  # Количество урн (слотов 2^Q)
    results = monte_carlo_simulation(num_trials, num_balls, num_urns)

    print("Средние количества урн:")
    print(f" - Пустых: {results[0]:.6f}")
    print(f" - С одним шариком: {results[1]:.6f}")
    print(f" - С двумя и более шариками: {results[2]:.6f}\n")

    print("Вероятности:")
    print(f" - Урна пустая: {results[3]:.6f}")
    print(f" - В урне ровно 1 шарик: {results[4]:.6f}")
    print(f" - В урне 2 и более шарика: {results[5]:.6f}")

