class Solution:
    def hammingWeight(self, n: int) -> int:
        n = format(n, 'b')
        count = 0
        print(n)
        for i in range(len(n)):
            if n[i] == '1':
                count += 1

        return count
