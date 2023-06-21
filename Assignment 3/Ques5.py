def plusOne(digits):
    n = len(digits)
    carry = 1

    for i in range(n - 1, -1, -1):
        digits[i] += carry
        digits[i] %= 10
        carry = digits[i] // 10

        if carry == 0:
            break

    if carry == 1:
        digits.insert(0, 1)

    return digits
digits = [1, 2, 3]
result = plusOne(digits)
print(result)  # Output: [1, 2, 4]