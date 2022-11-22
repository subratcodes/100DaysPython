class solution:

    def diagonaldifference(self, grid, N):

        sum = 0

        for x in range(0, N):
            print(grid[x][x])
            sum += grid[x][x]
            sum += grid[x][N - x - 1]

        return sum

    def transpose_matrix(self, grid, N):

        for x in range(0, N):

            for y in range(x+1, N):
            
                temp = grid[x][y]
        
                grid[x][y] = grid[y][x]
                grid[y][x] = temp
        print(grid)
