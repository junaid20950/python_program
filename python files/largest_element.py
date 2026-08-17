arr=[56,89,90,87,50,0,1,-1]
import math
def largest_element(arr):
    lar_ele = -math.inf
    for i in range(len(arr)):
        if arr[i] > lar_ele:
            lar_ele = arr[i]
    return lar_ele
print(f"largest element:{largest_element(arr)}")