s='machhine'
def isogram(s):
    output={}
    for i in range(len(s)):
        if s[i] in output:
            return False
        else:
            output[s[i]]=1
    return True
print(isogram(s))