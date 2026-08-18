num = 1004
def replace_zero(num):
    num_str = str(num)
    result =''
    for i in range(len(num_str)):
        if num_str[i] == '0':
            result += '5'
        else:
            result += num_str[i]
    return result
print(replace_zero(num))

    