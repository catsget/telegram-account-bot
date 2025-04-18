from numba import jit
from time import perf_counter

@jit(nopython=True, fastmath=True, cache=True)
def optimized_calculation(n):
    # Итеративный Фибоначчи
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    
    # Итеративный факториал
    fact = 1
    for i in range(1, n+1):
        fact *= i
    
    return b + fact

num = 40

start = perf_counter()
result = optimized_calculation(num)
end = perf_counter()

print(f"Результат: {result}")
print(f"Время выполнения: {end - start:.6f} сек")