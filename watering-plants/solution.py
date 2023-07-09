class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        water = capacity

        for i in range(len(plants)):
            if plants[i] <= water:
                water -= plants[i]
                steps += 1
            else:
                water = capacity
                water -= plants[i]
                steps += i + i + 1

        return steps
