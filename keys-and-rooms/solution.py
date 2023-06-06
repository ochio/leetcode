class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        stack = [rooms[0]]

        while stack:
            t = stack.pop()
            for r in t:
                if visited[r]:
                    continue
                else:
                    stack.append(rooms[r])
                    visited[r] = True
        return all(visited)
