n = int(input())
pairs = []

for i in range(n):
    left,right = map(int, input().split())
    pairs.append([left,right])

def longest_chain(pairs):
    pairs.sort(key=lambda x:x[1])

    count = 0
    curr_end = float('-inf')

    for left, right in range:
        if left > curr_end:
            count += 1
            curr_end = right

    return count

print(longest_chain(pairs))
