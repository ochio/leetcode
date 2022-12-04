class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiopQWERTYUIOP"
        second = "asdfghjklASDFGHJKL"
        third = "zxcvbnmZXCVBNM"
        ans = []

        for i in range(len(words)):

            self.f = True
            for j in range(len(words[i])):
                if words[i][j] not in first:
                    self.f = False
                    break
            if self.f:
                ans.append(words[i])
                continue

            self.f = True
            for j in range(len(words[i])):
                if words[i][j] not in second:
                    self.f = False
                    break
            if self.f:
                ans.append(words[i])
                continue

            self.f = True
            for j in range(len(words[i])):
                if words[i][j] not in third:
                    self.f = False
                    break
            if self.f:
                ans.append(words[i])
                continue
        return ans
