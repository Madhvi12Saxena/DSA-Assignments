'''Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
Input:  num1 = "11", num2 = "123"
Output: "134"'''

def addStrings(num1, num2):
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    result = ""

    while i >= 0 or j >= 0:
        digit_num1 = int(num1[i]) if i >= 0 else 0
        digit_num2 = int(num2[j]) if j >= 0 else 0

        digit_sum = carry + digit_num1 + digit_num2
        carry = digit_sum // 10
        result = str(digit_sum % 10) + result

        i -= 1
        j -= 1

    if carry > 0:
        result = str(carry) + result

    return result
num1 = "11"
num2 = "123"
sum_str = addStrings(num1, num2)

print(f"Sum: {sum_str}")