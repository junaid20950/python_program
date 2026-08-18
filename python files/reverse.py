s = "GeeksforGeeks"
# def reverse(s):
#     return s[::-1]
# print(f"reverse:{reverse(s)}")

def reverseii(s):
    start = len(s)-1
    end = -1
    interval = -1
    rev =''
    for i in range(start,end,interval):
    # for i in range(len(s)-1,-1,-1):
        rev+= s[i]
    return rev
# print(f"reverseii:{reverseii(s)}")
print(reverseii(s))
