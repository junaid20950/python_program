arr = [9, 7, 16, 16, 4]

def indexOfArray(arr):
    new_arr ={}
    for i in range(len(arr)):
        element = arr[i]
        if element in new_arr:
            new_arr[element].append(i)
        else:
            new_arr[element]=[i]
    return new_arr

print(indexOfArray(arr))