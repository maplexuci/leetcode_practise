from typing import List


class Solution:

    def oddCells(self, n: int, m: int, indices: List[List[str]]) -> int:
        matrix = [[0]*m for x in range(n)]
        for ls in range(len(indices)):
            r = indices[ls][0]
            c = indices[ls][1]
            matrix[r] = [x + 1 for x in matrix[r]]
            for i in range(len(matrix)):
                matrix[i][c] += 1

        cell = 0
        for a in range(len(matrix)):
            for b in matrix[a]:
                if b % 2 == 1:
                    cell += 1

        return cell


test = Solution()
num_odd_cell = test.oddCells(2, 3, indices=[[0, 1], [1, 1]])

print(num_odd_cell)
