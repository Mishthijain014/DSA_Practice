def reverse_string(s):
    if(len(s)<1):
        return ""
    else:
        first = s[0]
        rest = s[1:]
        return reverse_string(rest)+first
    
print(reverse_string("Mishthi"))