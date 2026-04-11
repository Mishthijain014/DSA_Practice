def sum_array(num):
    if(len(num)==0):
        return 0
    else:
        first =num[0]
        rest = num[1:]
        return sum_array(rest)+first
    
print(sum_array([1,2,3,4]))