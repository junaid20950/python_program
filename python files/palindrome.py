arr = [1, 2, 3, 3, 1]
def palindrome(arr):
    if arr==arr[::-1]:
        return True
    return False
print(palindrome(arr)) 