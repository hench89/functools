from functools import lru_cache

# example 1: least-recently-used cache
# lru cache can be used to keep recent or often-used data in memory by calculating once only.

@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

result = [fib(n) for n in range(16)]
print('calcualting fib sequence up to 16:', result)

# printing stats for the cache:
cache_info = fib.cache_info()
print('number of hits in the cache:', cache_info.hits)
print('number of misses/new insertion required:', cache_info.misses)
print('cache maxsize (default=128):', cache_info.maxsize)
print('cache current size:', cache_info.currsize)
