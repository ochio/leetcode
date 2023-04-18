import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x: x * (-1), nums))
        heapq.heapify(nums)

        c = 1
        while c < k:
            heapq.heappop(nums) * (-1)
            c += 1
        return heapq.heappop(nums) * (-1)
