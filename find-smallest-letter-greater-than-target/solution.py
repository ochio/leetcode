import bisect


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in range(len(letters)):
            letters[i] = ord(letters[i])

        target = ord(target)
        ind = bisect.bisect_right(letters, target)

        if ind == len(letters):
            return chr(letters[0])
        else:
            return chr(letters[ind])
