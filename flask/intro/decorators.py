import time

current_time = time.time()
#print(current_time)


def speed_calc_decorator(func):
    timenow = time.time()
    func()
    timeend = time.time()
    print(timeend-timenow)


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


slow_function
fast_function
