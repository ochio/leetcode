class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result = []
        for i in range(len(s)):
            c = 0
            row, col = startPos

            for j in range(i, len(s)):
                if s[j] == "R":
                    col += 1
                elif s[j] == "L":
                    col -= 1
                elif s[j] == "U":
                    row -= 1
                else:
                    row += 1

                if 0 <= col < n and 0 <= row < n:
                    c += 1
                else:
                    break
            result.append(c)

        return result
