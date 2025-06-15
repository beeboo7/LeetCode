class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        n = len(grid)

        for i in range(n):  # Loop through each row
            row = grid[i]

            for j in range(n):  # Loop through each column
                col = []

                for k in range(n):  # Build the column
                    col.append(grid[k][j])

                if row == col:
                    count += 1

        return count
