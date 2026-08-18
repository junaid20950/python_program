# num=[1,3,4,25,6,7,8,9,0,7,4,5,6,7,23]
s=1003
def replace_5(s):
    str_s=str(s)
    new_s=''
    for i in range(len(str_s)):
        if str_s[i]=='0':
            new_s+='5'
        else:
            new_s+=str_s[i]
    return new_s
print(replace_5(s))
