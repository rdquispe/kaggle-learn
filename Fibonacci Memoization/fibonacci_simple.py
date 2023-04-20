def fibonacci(number):
    if number == 1:
        return 1
    elif number == 2:
        return 1
    elif number > 2:
        return fibonacci(number - 1) + fibonacci(number - 2)


for n in range(1, 101):
    print(n, ":", fibonacci(n))
