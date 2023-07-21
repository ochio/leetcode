class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        same = []
        more = []

        for num in nums:
            if num == pivot:
                same.append(num)
            elif num > pivot:
                more.append(num)
            else:
                less.append(num)

        return less + same + more
