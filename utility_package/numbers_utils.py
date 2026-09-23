def is_prime(a,n):
    if a <= 1:
        return False
    
    for i in range(2,n):
        if n % i == 0:
            return False
        
    return True

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)