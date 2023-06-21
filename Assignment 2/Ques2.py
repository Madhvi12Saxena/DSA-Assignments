def max_candies(candyType):
    unique_candies = set(candyType)
    max_candies = len(candyType) // 2

    if len(unique_candies) <= max_candies:
        return len(unique_candies)
    else:
        return max_candies
candyType = [1, 1, 2, 2, 3, 3]
print(max_candies(candyType))