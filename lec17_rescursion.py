def factorial(n):
    if (n == 0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
            


print(factorial(4)) 
print(fibonacci(5))   
    