class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        def rec(cand, target, p):
            if target == 0:
                res.append(cand)
                return

            for i in range(p, len(candidates)):
                if i > p and candidates[i] == candidates[i - 1]:
                    continue

                pick = candidates[i]
                if target - pick < 0:
                    break
                rec(cand + [pick], target - pick, i + 1)

        res = []

        rec([], target, 0)
        return res
