class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        m = max(costs)
        ary = [0] * (m + 1)
        rst = [0] * len(costs)

        for cost in costs:
            ary[cost] += 1

        for i in range(1, len(ary)):
            ary[i] += ary[i - 1]

        i = len(costs) - 1
        while i >= 0:
            index = costs[i]
            rst[ary[index] - 1] = costs[i]
            ary[index] -= 1
            i -= 1

        c = 0
        for i in range(len(rst)):
            if coins < rst[i]:
                break
            else:
                c += 1
                coins -= rst[i]

        return c
