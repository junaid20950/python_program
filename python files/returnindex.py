k = 16
arr = [9, 7, 16, 16, 4]

def returnIndex(arr,k):
    output=0
    for i in range(len(arr)):
        if k == arr[i]:
            output=i
        else:
            output=-1
    return output
print(returnIndex(arr,k))

def returnIndexii(arr,k):
    output=0
    for i in range(len(arr)):
        if k in arr:
            output=arr.index(k)
        else:
            output=-1
    return output
print(returnIndexii(arr,k))