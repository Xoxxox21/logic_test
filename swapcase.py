def swap_case(s):
    data=''
    for i in range(len(s)):
        if s[i].islower():
            data=data+s[i].upper()
        elif s[i].isupper():
            data=data+s[i].lower()
        else:
            data=data+s[i]                   
    return data

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)