class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        w = s[0:k]
        vowels = w.count("a") + w.count("i") + w.count("u") + \
            w.count("e") + w.count("o")
        m = vowels

        for i in range(k, len(s)):
            left = s[i-k]
            right = s[i]

            if left == "a" or left == "i" or left == "u" or left == "e" or left == "o":
                vowels -= 1
            if right == "a" or right == "i" or right == "u" or right == "e" or right == "o":
                vowels += 1

            m = max(m, vowels)
        return m
