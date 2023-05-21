from math import inf


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = inf, inf

        for third in nums:

            if second < third:
                return True
            elif third <= first:
                first = third
            elif first < third < second:
                second = third
        return False
