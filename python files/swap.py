arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 7
def swapkth(arr,k):
    for i in range(1,len(arr)+1):
        if i==k:
            arr[k-1],arr[-k]=arr[-k],arr[k-1]
    return arr
print(swapkth(arr,k))