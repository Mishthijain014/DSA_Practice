def sum_n(n):
    if(n==0):
        return 0
    else:
        return sum_n(n-1)+n

print(sum_n(5))