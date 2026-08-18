arr=[56,89,90,87,50,3,0,-1]
import math
def second_largest(arr):
    lar = -math.inf
    sec_lar = -math.inf
    for i in arr:
        if i > lar:
            sec_lar = lar
            lar = i
        elif i > sec_lar and i!=lar:
            sec_lar = i
    return sec_lar
print(f"Second Largest:{second_largest(arr)}")