import time
import Suma

"""
Podajemy kolejny argument ile razy funkcja mierząca czas ma zostać wykonana i domyślne ustawiamy 1 aby gdy nie podamy ile razy ma zostać wywołana funkcja zostało przyjęte domyślne 1 aby wykonała się jeden raz
"""
def function_performance(func, arg, how_many_times = 1):

    sum = 0

    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end-start)

    return sum



print(function_performance(Suma.sumuj_do,50000,5))
print(function_performance(Suma.sumuj_do2,50000))
print(function_performance(Suma.sumuj_do3,50000))
print(function_performance(Suma.sumuj_do4,50000))
print(function_performance(Suma.sumuj_do5,50000))

