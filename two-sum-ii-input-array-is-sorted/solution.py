class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def bs(l, r, v):
            left = l
            right = r
            while left <= right:
                middle = (left + right) // 2

                if numbers[middle] == v and middle == l:
                    left = left + 1
                    continue
                if numbers[middle] == v:
                    return middle
                elif numbers[middle] < v:
                    left = middle + 1
                else:
                    right = middle - 1

            return -1

        for i in range(len(numbers)):
            v = target - numbers[i]
            l = i
            r = len(numbers) - 1

            a = bs(l, r, v)
            if a != -1:
                return [l + 1, a + 1]
