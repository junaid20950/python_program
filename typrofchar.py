s = "#GeeKs01fOr@gEEks07"
def typeofchar(s):
    l_case = 0
    u_case = 0
    spcl_char = 0
    num_value = 0
    for i in range(len(s)):
        if s[i].islower():
            l_case+=1
        elif s[i].isupper():
            u_case+=1
        elif s[i].isnumeric():
            num_value+=1
        else:
            spcl_char+=1
    return f"l_case:{l_case}\nu_case:{u_case}\nspcl_char:{spcl_char}\nnum_value:{num_value}"

print(typeofchar(s))