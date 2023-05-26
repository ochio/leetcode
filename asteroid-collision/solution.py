class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for num in asteroids:
            if len(stack) > 0 and num < 0 and stack[-1] > 0:
                if abs(num) < abs(stack[-1]):
                    continue
                elif abs(num) > abs(stack[-1]):
                    while len(stack) > 0 and stack[-1] > 0 and abs(num) > abs(stack[-1]):
                        stack.pop()

                    if len(stack) > 0 and stack[-1] > 0 and abs(num) == abs(stack[-1]):
                        stack.pop()
                        continue
                    elif len(stack) > 0 and stack[-1] > 0 and abs(num) < abs(stack[-1]):
                        continue
                else:
                    stack.pop()
                    continue
            stack.append(num)

        return stack
