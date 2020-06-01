# This is my functions module

# Checks in the input number is prime or not
def isprime(num):
    if type(num) != int:
        try:
            num = int(num)
        except ValueError:
            return "Invalid input value."

    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return str(num) + " is not a prime number" + "\n" + str(i) + " times " +  str(num//i) + " is " + str(num)

        else:
            return str(num) + " is a prime number"

    else:
        return str(num) + " is not a prime number"

# Returns fibonacci numbers up to n
def fib(n):
    if type(n) != int:
        try:
            n = int(n)
        except ValueError:
            return "Invalid input value."

    fib1, fib2 = 0, 1
    result = []
    while fib1 < n:
        result.append(fib1)
        fib1, fib2 = fib2, fib1 + fib2
    return f"Fibonacci numbers up to {n} are: " + str(result)[1:-1]
