n=9
def prime(n):
    h=2
    j=n//2
    for i in range(h,j):
        if n%i==0:
            return False
    return True
print(prime(9))