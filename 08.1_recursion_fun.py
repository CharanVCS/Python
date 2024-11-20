#code to find factorial of number
def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

a = int(input('Enter your numder:'))

print(factorial(a))
