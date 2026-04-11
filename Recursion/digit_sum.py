def digit_sum(num):

    if(num<10):
        return num

    s = num%10
    return s+ digit_sum(num//10)

print(digit_sum(321))
    