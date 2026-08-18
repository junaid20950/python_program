s='Geeks87'
def delete_odd(s):
    
    odds = ''
    for i in range(len(s)):
        if i%2==0:
            odds += s[i]
    return odds  
print(delete_odd(s))

output = s[1::2] #string slicing with the syntax s[start:stop:step]: