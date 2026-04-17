def count_down(n):
    if(n==0):
        return
    else:
        print(n)
        count_down(n-1)

count_down(5)