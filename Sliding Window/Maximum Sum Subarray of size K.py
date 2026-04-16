def sum_subarray(arr,k):
    n = len(arr)

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k,n):
        window_sum += arr[i]
        window_sum -= arr[i-k]

        max_sum = max(window_sum,max_sum)

    return max_sum
sum_subarray([],0)
print(sum_subarray([1,2,3,4,5,6],3))