num = 6
def sumofnum(n):
    return sum(range(1, n+1))

def sumofnum_ii(n):
    total = 0
    print(range(n+1))
    for i in range(n+1):        
        total += i
    return total
print(f"sumofnum:{sumofnum(6)}")
print(f"sumofnumii: {sumofnum_ii(6)}")