class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        i = 0
        j = 1
        total = 0
        while i < len(timeSeries):
            if j >= len(timeSeries):
                total += duration
                break
            if timeSeries[i] + duration < timeSeries[j]:
                total += duration
            else:
                total += timeSeries[j] - timeSeries[i]
            i = j
            j += 1
        return total
