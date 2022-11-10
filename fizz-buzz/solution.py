class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            s = ""
            if i % 15 == 0:
                s = "FizzBuzz"
            elif i % 3 == 0:
                s = "Fizz"
            elif i % 5 == 0:
                s = "Buzz"
            else:
                s = str(i)

            ans.append(s)
        return ans
