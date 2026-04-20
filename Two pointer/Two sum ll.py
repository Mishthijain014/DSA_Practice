numbers = [2,7,11,15]
target = 18
left = 0
right = len(numbers) - 1

while left < right:
    current_sum = numbers[left] + numbers[right]
            
    if current_sum == target:
        print(left+1,right+1)
        break            
    elif current_sum < target:
        left += 1
    else:
        right -= 1
