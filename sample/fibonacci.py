from functools import cache


@cache
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

import time
start = time.time()
print(fibonacci(100))
end = time.time()

print("The time of execution of above program is :", end - start)
