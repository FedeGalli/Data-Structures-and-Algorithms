def stepsCounter(grid, posx, posy, steps):
    
    if posx == len(grid) and posy == len(grid[0]):
        return steps
    
    if posx < len(grid) and posy < len(grid[0]):
        if grid[posx][posy] == 1:
            print(posx, posy)
            stepsCounter(grid, posx + 1, posy, steps + 1)
            stepsCounter(grid, posx, posy + 1, steps + 1)
    

grid = [[1] * 3] * 3

print(stepsCounter(grid, 0, 0, 0))

