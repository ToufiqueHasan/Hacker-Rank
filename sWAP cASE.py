def swap_case(s):
    x=""
    for i in range(len(s)):
        if s[i]>='A' and s[i]<='Z':
            x=x+s[i].lower()
        else:
            x=x+s[i].upper()
    return x


if __name__ == "__main__":
    s = input()
    result=swap_case(s)
    print(result)
    
