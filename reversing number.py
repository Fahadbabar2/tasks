def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

num = int(input("Enter a number"))
print("Factorial is", factorial(num))
