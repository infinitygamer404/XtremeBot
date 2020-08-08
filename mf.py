import time
import datetime

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
                return f"{num} is not a prime number\n{i} times {num//i} is {num}"

        else:
            return f"{num} is a prime number"

    else:
        return f"{num} is not a prime number"

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
    return f"Fibonacci numbers up to {n} are: {str(result)[1:-1]}"

# Logs different events for the bot
def log(msg="", trig=0, cmd="", resp="", user=""):
    # Time and Date formatting
    s = str(time.asctime(time.gmtime(time.time() + 21600)))
    t = datetime.datetime.strptime(s, "%a %b  %d %H:%M:%S %Y")
    t = t.strftime("%a %d/%m/%Y  %I:%M:%S %p")
    
    # Response to trigger 0. Log start.
    if trig == 0:
        s = f"[Bot has been connected to Discord] [Started logging at: '{t}']"
    
    # Response to trigger 1. Manual log.
    if trig == 1:
        s = f"[Manual log at: '{t}'] [Message: '{msg}']"
    
    # Response to trigger 2. Comman log.
    if trig == 2:
        s = f"['{user}' triggered '{cmd}' command at: '{t}'] [Message: '{msg}'] [Response: '{resp}']"
        
    # Writing the log to a file.
    f = open("log.log", "a+")
    f.write(s+"\n")
    f.close()
