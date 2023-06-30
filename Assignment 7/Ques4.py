'''Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
Input: s = "Let's take LeetCode contest"
Output:  "s'teL ekat edoCteeL tsetnoc"'''

def reverseWords(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    reversed_s = " ".join(reversed_words)
    return reversed_s
s = "Let's take LeetCode contest"
reversed_s = reverseWords(s)

print(f"Reversed: {reversed_s}")