import random


def monte_carlo_simulation(num_trials, num_balls, num_urns):
    empty_counts = []
    one_ball_counts = []
    multiple_ball_counts = []

    for _ in range(num_trials):
        # Список для подсчёта количества шариков в каждой урне
        urns = [0] * num_urns

        # Распределяем шарики случайным образом по урнам
        for _ in range(num_balls):
            urn_choice = random.randint(0, num_urns - 1)
            urns[urn_choice] += 1

        # Считаем, сколько урн в каждом из состояний
        empty_count = urns.count(0)  # Количество пустых урн
        one_ball_count = urns.count(1)  # Количество урн с одним шариком
        multiple_ball_count = num_urns - empty_count - one_ball_count  # Остальные урны

        # Сохраняем результаты для текущего эксперимента
        empty_counts.append(empty_count)
        one_ball_counts.append(one_ball_count)
        multiple_ball_counts.append(multiple_ball_count)

    # Вычисляем средние значения
    avg_empty = sum(empty_counts) / num_trials
    avg_one_ball = sum(one_ball_counts) / num_trials
    avg_multiple_ball = sum(multiple_ball_counts) / num_trials

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

