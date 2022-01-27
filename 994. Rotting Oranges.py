Problem :''' 994. Rotting Oranges
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        visited = set()
        fresh = 0
        rotten = deque([])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        
        if fresh == 0:
            return 0
        
        def bfs(q, ans, fresh):
            while q:
                lenq = len(q)
                for i in range(lenq):
                    i, j = q.popleft()
                    for tx, ty in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                        nx = tx + i
                        ny = ty + j

                        if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            fresh -= 1
                            q.append((nx, ny))
                            
                    
                
                ans += 1
            
            return -1 if fresh else ans
        
        return bfs(rotten, -1, fresh)
