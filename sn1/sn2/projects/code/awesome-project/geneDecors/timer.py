import time


def timer(func):
    def wrapper(*args, *kwargs):
        start = time.time()
        result = funct(*args, *kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return func
    return wrapper


@timer
def slow_function():
    time.sleep(2)
    print("Finished")


slow_function()
