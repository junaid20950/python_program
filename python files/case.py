s = 'fsgahfsgTGV'
def uppercase(s):
    for i in range(len(s)):
          if s[i].islower():
            return False 
    return False

def updatecaseupper(s):
    new_s = ''
    for i in range(len(s)):
        if s[0].islower():
            new_s+=s[i].lower()
        else:
            new_s+=s[i].upper()
    return new_s
# print(uppercase(s))
print(updatecaseupper(s))