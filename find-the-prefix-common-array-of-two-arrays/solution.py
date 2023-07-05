class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a_set = set()
        b_set = set()
        result = []

        for i in range(len(A)):
            a_set.add(A[i])
            b_set.add(B[i])
            result.append(len(a_set & b_set))

        return result
