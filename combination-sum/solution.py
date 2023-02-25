import copy


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        stack = []
        for i in candidates:
            if target >= i:
                stack.append([i])

        ans = []
        while stack:
            l = stack.pop(0)
            r = target - sum(l)

            if r == 0:
                ans.append(l)
                continue

            for i in candidates:
                t = copy.deepcopy(l)
                if i < t[-1]:
                    continue
                if r - i > 0:
                    t.append(i)
                    stack.append(t)
                elif r - i < 0:
                    break
                else:
                    t.append(i)
                    ans.append(t)
                    break

        return ans
