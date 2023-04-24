from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Solution from user hiepit in LeetCode Solutions
        Date: 4/24/2023
        Source: "https://leetcode.com/problems/01-matrix/solutions/1369741/c-java-python-bfs-dp-solutions-with-picture-clean-concise-o-1-space/?envType=study-plan&id=algorithm-i&orderBy=most_votes"
        """
        m, n = len(mat), len(mat[0])
        DIR = [0, 1, 0, -1, 0]

        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1  # Marked as not processed yet!

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][
                    nc] != -1: continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
        return mat
