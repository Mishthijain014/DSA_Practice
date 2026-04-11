def is_palindrom(s):
    palindrom = True
    if(len(s)<=1):
        return palindrom
    if(s[0] != s[-1]):
        palindrom = False
        return palindrom
    else:
        new = s[1:-1]
        return is_palindrom(new)
    
print(is_palindrom("madam"))
