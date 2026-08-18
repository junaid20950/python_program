arr=[56,89,90,87,50,3,0,-1]
def smallest_element(arr):
    import math
    sml_ele = math.inf
    for i in arr:
        if i<sml_ele:
            sml_ele = i
    return sml_ele
print(f"Smallest Element:{smallest_element(arr)}")