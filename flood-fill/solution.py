class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        tc = image[sr][sc]
        t = [[False for i in range(len(image[0]))] for j in range(len(image))]

        stack = [[sr, sc]]
        t[sr][sc] = True

        d = [[-1, 0], [0, -1], [0, 1], [1, 0]]

        while stack:
            [current_y, current_x] = stack.pop()

            for i in d:
                next_y = current_y + i[0]
                next_x = current_x + i[1]
                if 0 <= next_x < len(image[0]) and 0 <= next_y < len(image):
                    if t[next_y][next_x]:
                        continue
                    elif image[next_y][next_x] == tc:
                        t[next_y][next_x] = True
                        stack.append([next_y, next_x])

        for i in range(len(t)):
            for j in range(len(t[0])):
                if t[i][j]:
                    t[i][j] = color
                else:
                    t[i][j] = image[i][j]

        return t
