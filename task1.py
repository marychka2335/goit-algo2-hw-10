import random
import timeit
import matplotlib.pyplot as plt

# Визначення функцій сортування
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quick_sort(less) + equal + randomized_quick_sort(greater)

def deterministic_quick_sort(arr, pivot_choice='center'):
    if len(arr) <= 1:
        return arr
    if pivot_choice == 'start':
        pivot = arr[0]
    elif pivot_choice == 'end':
        pivot = arr[-1]
    else:  # 'center'
        pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return deterministic_quick_sort(less, pivot_choice) + equal + deterministic_quick_sort(greater, pivot_choice)

# Генерація випадкових масивів
def create_random_array(n):
    return [random.randint(0, n) for _ in range(n)]

# Вимірювання часу сортування
def measure_sort_times(arr, sort_func, pivot_choice=None):
    if pivot_choice:
        return timeit.timeit(lambda: sort_func(arr[:], pivot_choice), number=5) / 5
    return timeit.timeit(lambda: sort_func(arr[:]), number=5) / 5

# Тестування часу сортування для різних розмірів масивів
def test_sort_times(length):
    arr = create_random_array(length)
    print_width = 50
    print('\n' + f' Starting tests for length: {length/1000:.0f}k '.center(print_width, '-'))
    time_sort_random = measure_sort_times(arr, randomized_quick_sort)
    print(f'{"Time of quick sort (pivot = random):":<37} {time_sort_random:.4f}s'.center(print_width))
    time_sort_start = measure_sort_times(arr, deterministic_quick_sort, 'start')
    print(f'{"Time of quick sort (pivot = start):":<37} {time_sort_start:.4f}s'.center(print_width))
    time_sort_end = measure_sort_times(arr, deterministic_quick_sort, 'end')
    print(f'{"Time of quick sort (pivot = end):":<37} {time_sort_end:.4f}s'.center(print_width))
    time_sort_center = measure_sort_times(arr, deterministic_quick_sort, 'center')
    print(f'{"Time of quick sort (pivot = center):":<37} {time_sort_center:.4f}s'.center(print_width))
    print(f' Finished 5 tests each '.center(print_width, '-'))
    return {
        'time_sort_random': time_sort_random,
        'time_sort_start': time_sort_start,
        'time_sort_end': time_sort_end,
        'time_sort_center': time_sort_center
    }

if __name__ == '__main__':
    time_start = timeit.default_timer()
    times_10k = test_sort_times(10_000)
    times_50k = test_sort_times(50_000)
    times_100k = test_sort_times(100_000)
    times_500k = test_sort_times(500_000)
    times_rand = [times_10k['time_sort_random'], times_50k['time_sort_random'], times_100k['time_sort_random'], times_500k['time_sort_random']]
    times_start = [times_10k['time_sort_start'], times_50k['time_sort_start'], times_100k['time_sort_start'], times_500k['time_sort_start']]
    times_end = [times_10k['time_sort_end'], times_50k['time_sort_end'], times_100k['time_sort_end'], times_500k['time_sort_end']]
    times_center = [times_10k['time_sort_center'], times_50k['time_sort_center'], times_100k['time_sort_center'], times_500k['time_sort_center']]
    total_time = timeit.default_timer() - time_start
    print(f'\nTotal time taken: {total_time:.4f}s\n')

    # Побудова графіка
    labels = ['10_000', '50_000', '100_000', '500_000']
    plt.plot(labels, times_rand, label='Randomized QuickSort')
    plt.plot(labels, times_start, label='Deterministic QuickSort (Start)')
    plt.plot(labels, times_end, label='Deterministic QuickSort (End)')
    plt.plot(labels, times_center, label='Deterministic QuickSort (Center)')
    plt.legend(title='Pivot location', title_fontproperties={'weight': 'bold'})
    plt.xlabel('Array length')
    plt.ylabel('Time (s)')
    plt.title('Sorting times for QuickSort variants')
    plt.grid(True)
    plt.show()
