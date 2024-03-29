import pygame
from pygame.locals import *
import numpy as np
from random import randint as ri
#import sys
#np.set_printoptions(threshold=sys.maxsize)

def draw(screen, grid, grid_n, r_n, c_n, MARGIN, WIDTH, HEIGHT, rev, font, dr_txt):
    if rev is True:
        c_n, r_n = r_n, c_n
    for row in range(r_n):
        for column in range(c_n):
            color = BLACK
            if rev is False:
                gr = grid[row][column]
                grn = grid_n[row][column]
            elif rev is True:
                gr = grid[column][row]
                grn = grid_n[column][row]

            if gr == 1:
                color = GREEN
            elif gr == 2:
                color = RED

            rec = [(int(MARGIN+WIDTH)*column+MARGIN), (int(MARGIN+HEIGHT)*row+MARGIN), (WIDTH), (HEIGHT)]
            pygame.draw.rect(screen, color, rec)
            if dr_txt is True:
                text = font.render(str(grn), 1, WHITE)
                screen.blit(text, rec)
     
    return screen
 
def check(grid, r, c):
    num = 0
    for ri in range(-1,2):
        for ci in range(-1,2):
            bo = True
            if ri == 0 and ci == 0:pass
            else:
                try:
                    if r+ri < 0 or c+ci < 0:
                        bo = False
                    if grid[r+ri][c+ci] != 0 and bo is True:
                        num += 1
                    if __name__ != "__main__" and bo is True: 
                        print(grid[r+ri][c+ci], r+ri, c+ci, end="\n")
                except Exception:pass
    #if __name__ != "__main__":
        #print()
    return num

def n_che(num, ar):
    bo = False
    for i in ar:
        if num == i:
            bo = True
    return bo

if __name__ == "__main__":
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GRAY = (127, 127, 127)
    
    rev = bool( 0 )

    b_val = [3] #[3, 6, 7, 8]

    s_val = [2, 3] #[3, 4, 6, 7, 8]
    
    MARGIN = 1
     
    pygame.init()
     
    WINDOW_SIZE = (1540, 801) #(2340, 1080)
    #WINDOW_SIZE = WINDOW_SIZE[::-1]
    screen = pygame.display.set_mode(WINDOW_SIZE, RESIZABLE)
    
    mul = 0.35#1875
    WIDTH = 100*mul
    HEIGHT = 100*mul
    
    c_n = (WINDOW_SIZE[0]/WIDTH)
    r_n = (WINDOW_SIZE[1]/HEIGHT)
    c_ni, r_ni = int(c_n), int(r_n)
    print(c_n, r_n)

    font = pygame.font.SysFont("arial", int(min(WIDTH, HEIGHT)))
    
    clock = pygame.time.Clock()

    if rev is True:
        c_n, r_n = r_n, c_n
        
    grid = [ [ 0 for _ in range(c_ni)] for _ in range(r_ni)]
    grid_n = [ [ 0 for _ in range(c_ni)] for _ in range(r_ni)]
    
    pygame.display.set_caption("Array Backed Grid")

    done = False
    press = False
    pau = True
    step = False
    free = False
    dr_txt = False
    prin = False
    pen = True
    rand = False
    co = 0
    speed = 0
    
    if rand is True:
        grid = [ [ ri(0,1) for _ in range(c_ni)] for _ in range(r_ni)]
        #grid_n = [ [ ri(0,1) for _ in range(c_n)] for _ in range(r_n)]

    gr_po = [[11,2],[10,2],[10,3],[11,3],[10,13],[9,13],[11,13],[12,14],[13,15],[12,16],[11,17],[10,17],[11,18],[10,18],[9,18],
             [9,17],[10,17],[8,16],[7,15],[8,14],[9,23],[8,23],[9,24],[9,25],[9,26],[8,26],[7,26],[7,25],[7,24],[7,23],[6,24],
             [6,25],[6,26],[6,27],[5,27],[10,24],[10,25],[10,26],[10,27],[11,27],[9,36], [8,36], [8,37], [9,37],]

    for i,j in gr_po:
        grid[i][j] = 1
    
    start_grid = grid.copy()
    #print(np.array(start_grid))
    grido = grid.copy()


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pau = not pau
                if event.key == K_ESCAPE:
                    done = True
                if event.key == K_c:
                    grid = [ [ 0 for _ in range(c_ni)] for _ in range(r_ni)]
                if event.key == K_r:
                    if rand is True:
                        grid = [ [ ri(0,1) for _ in range(c_ni)] for _ in range(r_ni)]
                    else:
                        grid = [ [ 0 for _ in range(c_ni)] for _ in range(r_ni)]
                        for i,j in gr_po:
                            grid[i][j] = 1
                if event.key == K_a:
                    speed += 10
                if event.key == K_s:
                    speed -= 10
                    if speed < 0:
                        speed = 0
                if event.key == K_n:
                    step = True
                    pau = False
                if event.key == K_f:
                    free = not free
                if event.key == K_p:
                    pen = not pen

            if event.type == pygame.MOUSEBUTTONDOWN:
                press = True
            elif event.type == pygame.MOUSEBUTTONUP:
                press = False

                
            if press is True:
                pos = pygame.mouse.get_pos()
                colu = pos[0]/(WIDTH+MARGIN)
                ro = pos[1]/(HEIGHT+MARGIN)
                if rev is True and prin is True:
                    print(f"[{int(colu)},{int(ro)}],", end=' ')
                    colu, ro = ro, colu
                elif prin is True:
                    print(f"[{int(ro)},{int(colu)}],", end=' ')
                ir, ic = int(ro), int(colu)

                try:
                    if pen is True and grid[ir][ic] == 0:
                        grid[ir][ic] = 2
                    elif pen is False and grid[ir][ic] != 0:
                        grid[ir][ic] = 0
                except Exception:pass

        
        #clock.tick(speed)
        run = False
        if free is False and pau is True:
            run = True
        elif free is False and pau is False:
            pygame.time.wait(speed)
        if free is True and pau is True:
            run = True

        screen = draw(screen, grid, grid_n, r_ni, c_ni, MARGIN, WIDTH, HEIGHT, rev, font, dr_txt)
        if run is False:
            for r in range(r_ni):
                for c in range(c_ni):
                    num = check(grid, r, c)
                    grid_n[r][c] = num

            grido = grid.copy()
            for r in range(r_ni):
                for c in range(c_ni):
                    num = grid_n[r][c]
                    if grido[r][c] == 2:
                        grid[r][c] = 1
                    if grido[r][c] == 0 and n_che(num, b_val):
                        grid[r][c] = 2
                    if grido[r][c] != 0 and n_che(num, s_val):pass
                    else:
                        grid[r][c] = 0

        if free is False and step is True:
            pau = True
            step = False

        pygame.display.update()
        screen.fill(GRAY)
        co += 1

    pygame.quit()