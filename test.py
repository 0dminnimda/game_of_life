from grid_field import check
from random import randint as ri
import numpy as np
c_n = r_n = 3
grid = [ [ i*10+j for j in range(c_n)] for i in range(r_n)]
print(np.array(grid))
for i in range(3):
     for j in range(3):
        print(grid[i][j])
        num = check(grid, i, j)
        print(num)
        print()