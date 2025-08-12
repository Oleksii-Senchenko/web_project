import threading
import time

def decorator(label):
    def time_decorator(func):
        def wrapper(*args, **kwargs):

            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()

            print(f"{label} took {end - start:.4f} seconds.")
            return result
        return wrapper
    return time_decorator


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True



@decorator("Single_thread")
def find_primes_single_thread(start, end, result):
    numbers = []
    for i in range(start, end + 1):
        if is_prime(i):
            numbers.append(i)
    result.extend(numbers)


@decorator("Multi_thread")
def find_primes_multi_thread(start, end):
    middle = (start + end) // 2
    result1 = []
    result2 = []

    thread1 = threading.Thread(target=find_primes_single_thread, args=(start, middle, result1))
    thread2 = threading.Thread(target=find_primes_single_thread, args=(middle + 1, end, result2))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    result = result1 + result2

    return result

result_list = []
find_primes_single_thread(2, 10, result_list)

print(find_primes_multi_thread(2, 10))


def test_same_result():
    start = 2
    end = 100

    single_thread_test_list = []
    find_primes_single_thread(start, end, single_thread_test_list)

    multi_threading_result = find_primes_multi_thread(start, end)

    assert sorted(single_thread_test_list) == sorted(multi_threading_result), "Test for same result not match"

    print("Test for same result is passed")
