def findMissingRanges(nums, lower, upper):
    ranges = []
    prev = lower - 1

    for num in nums + [upper + 1]:
        if num == prev + 2:
            ranges.append([prev + 1, prev + 1])
        elif num > prev + 2:
            ranges.append([prev + 1, num - 1])
        prev = num

    return ranges
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99

print(findMissingRanges(nums, lower, upper))