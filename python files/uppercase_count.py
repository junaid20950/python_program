s = 'fgaTrnbcnION'
def find_uppercase(s):
    new_s = ''
    count = 0
    for i in range(len(s)):
        if s[i].islower():
            new_s+=s[i]
            count+=1
    return [new_s,count]
print(f"Find Uppercase:{find_uppercase(s)}")