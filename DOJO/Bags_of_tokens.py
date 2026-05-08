def bags_of_tokens(tokens,power):
    tokens.sort()

    left = 0
    right = len(tokens) - 1

    score = 0
    max_score = 0

    while left <= right:
        if power >= tokens[left]:
            score += 1
            power -= tokens[left]

            max_score = max(max_score,score)

            left += 1

        elif score > 0:
            score -= 1
            power += tokens[right]

            right -= 1

        else:
            break

    return max_score

print(bags_of_tokens([100,200,300,400],200))