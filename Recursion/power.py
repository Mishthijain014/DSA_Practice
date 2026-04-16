# SOLUTION 1

# def power(x,n):
#     if(n==0):
#         return 1
#     else:
#         return x*power(x,n-1)

# print(power(2,3))



# SOLUTION 2

def power(x,n):
    if(n==0):
        return 1
    if(n==1):
        return x
    if(n<0):
        n = -n
        x = 1/x

    half = power(x,n//2)
    
    if n%2==2:
        return half * half
    else:
        return x*half*half
    
print(power(2,3))






