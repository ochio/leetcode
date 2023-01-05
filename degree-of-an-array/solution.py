from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = defaultdict(lambda: defaultdict(int))

        for i in range(len(nums)):
            d[nums[i]]["count"] += 1
            if d[nums[i]]["start"] == 0 and nums[i] != nums[0]:
                d[nums[i]]["start"] = i
            d[nums[i]]["end"] = i

        t = nums[0]

        for k in d.keys():
            if d[t]["count"] < d[k]["count"]:
                t = k
            elif d[t]["count"] == d[k]["count"]:
                tl = d[t]["end"] - d[t]["start"]
                kl = d[k]["end"] - d[k]["start"]
                if tl > kl:
                    t = k
        return d[t]["end"] - d[t]["start"] + 1
