fibonacci_cache = {}


def fibonacci(number):
    # If we have chached the value, then return it
    if number in fibonacci_cache:
        return fibonacci_cache[number]
    # Compute the Nth term
    if number == 1:
        return 1
    elif number == 2:
        return 1
    elif number > 2:
        value = fibonacci(number - 1) + fibonacci(number - 2)
    # Cache the value and return it
    fibonacci_cache[number] = value
    return value


for n in range(1, 101):
    print(n, ":", fibonacci(n))
