'''Given two strings s and p, return *an array of all the start indices of* p*'s anagrams in* s. You may return the answer in **any order**.
An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".'''

from collections import Counter

def findAnagrams(s, p):
    target_freq = Counter(p)
    window_freq = Counter()
    left = 0
    matched = 0
    result = []

    for right in range(len(s)):
        # Add the current character to the window
        window_freq[s[right]] += 1

        # Increment the count of matched characters
        if window_freq[s[right]] <= target_freq[s[right]]:
            matched += 1

        # Check if the current window is of size equal to the length of p
        if right - left + 1 == len(p):
            # Check if the current window is an anagram of p
            if matched == len(p):
                result.append(left)

            # Remove the character at the left pointer from the window
            window_freq[s[left]] -= 1
            if window_freq[s[left]] < target_freq[s[left]]:
                matched -= 1

            # Move the left pointer to the right
            left += 1

    return result
s = "cbaebabacd"
p = "abc"
result = findAnagrams(s, p)
print(result)