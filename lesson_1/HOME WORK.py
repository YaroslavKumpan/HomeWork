import time

def cached_with_ttl(ttl_seconds):
    def decorator(func):
        cache = {}

        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            if key in cache and time.time() - cache[key][1] < ttl_seconds:
                return cache[key][0]

            result = func(*args, **kwargs)
            cache[key] = (result, time.time())
            return result

        def cache_get(key):
            return cache.get(key)

        wrapper.cache_get = cache_get
        return wrapper

    return decorator


@cached_with_ttl(ttl_seconds=5)
def example_function(x):
    print("Выполнение функции...")
    return x * 2

result_1 = example_function(3)
print(result_1)

result_2 = example_function(3)
print(result_2)

time.sleep(6)

result_3 = example_function(3)
print(result_3)