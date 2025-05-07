import multiprocessing
import time

def calc_factofrial(n):
    res = 1
    for i in range(1, n+1):
        print(i)
        print(res)
        res *= i
        print("")
    return res
print(calc_factofrial(5))

def factorials_in_parallel(nums):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        res = pool.map(calc_factofrial, nums)
    return res

if __name__ == "__main__":
    numbers = list(range(1000, 1051))  
    start_time = time.time()
    results_parallel = factorials_in_parallel(numbers)
    end_time = time.time()
    parallel_time = end_time - start_time

    print(f"Время выполнения с многозадачностью: {parallel_time:.4f} sec")

    start_time = time.time()
    results_seq = [calc_factofrial(n) for n in numbers]
    end_time = time.time()
    seq_time = end_time - start_time
    print(f"Время выполнения без многозадачности: {seq_time:.4f} sec")
    print(f"Первые 5 с многозадачностью: {results_parallel[:5]}")
    print(f"Первые 5 без многозадачности: {results_seq[:5]}")

