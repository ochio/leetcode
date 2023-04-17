class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        a = []

        def rec(comb, idx):
            if len(comb) == k:
                if sum(comb) == n:
                    a.append(comb)
                return
            for i in range(idx, 10):
                rec(comb + [i], i + 1)

        rec([], 1)
        return a
