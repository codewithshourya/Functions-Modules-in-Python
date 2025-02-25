def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

Number = int(input("Enter a number: "))
Factorial = factorial(Number)
print(f"Factorial of {Number} is {Factorial}")