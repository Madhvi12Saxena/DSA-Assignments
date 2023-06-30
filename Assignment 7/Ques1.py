'''Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
Input: s = "egg", t = "add"
Output: true'''

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in s_to_t and s_to_t[char_s] != char_t:
            return False
        if char_t in t_to_s and t_to_s[char_t] != char_s:
            return False

        s_to_t[char_s] = char_t
        t_to_s[char_t] = char_s

    return True
s = "egg"
t = "add"
isomorphic = isIsomorphic(s, t)

print(f"Isomorphic: {isomorphic}")