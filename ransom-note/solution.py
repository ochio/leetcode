from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)

        for s in r_count:
            if r_count[s] > m_count[s]:
                return False

        return True

