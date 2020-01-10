import pygame
from pygame.locals import *
import numpy as np

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
                text = font.render(str(grn), 1, (0, 0, 0))
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

if __name__ == "__main__":
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GRAY = (127, 127, 127)
    
    rev = bool( 0 )

    b_val = 3
    s_val1 = 2
    s_val2 = 3
    
    MARGIN = 0.5
     
    pygame.init()
     
    WINDOW_SIZE = (1540, 801) #(2340, 1080)
    #WINDOW_SIZE = WINDOW_SIZE[::-1]
    screen = pygame.display.set_mode(WINDOW_SIZE, RESIZABLE)
    
    WIDTH = 100*0.375
    HEIGHT = 100*0.375
    
    c_n = int(WINDOW_SIZE[0]//WIDTH)
    r_n = int(WINDOW_SIZE[1]//HEIGHT)
    print(c_n, r_n)

    font = pygame.font.SysFont("arial", int(min(WIDTH, HEIGHT)))
    
    if rev is True:
        c_n, r_n = r_n, c_n
        
    grid = [ [ 0 for _ in range(c_n)] for _ in range(r_n)]
    grid_n = [ [ 0 for _ in range(c_n)] for _ in range(r_n)]
    
    pygame.display.set_caption("Array Backed Grid")
    
    done = False
    press = False
    pau = True
    step = False
    free = False
    dr_txt = False
    co = 0
    speed = 50
    
    gr_po = [[11,2],[10,2],[10,3],[11,3],[10,13],[9,13],[11,13],[12,14],[13,15],[12,16],[11,17],[10,17],[11,18],[10,18],[9,18],
             [9,17],[10,17],[8,16],[7,15],[8,14],[9,23],[8,23],[9,24],[9,25],[9,26],[8,26],[7,26],[7,25],[7,24],[7,23],[6,24],
             [6,25],[6,26],[6,27],[5,27],[10,24],[10,25],[10,26],[10,27],[11,27],[9,36], [8,36], [8,37], [9,37],]
    for i,j in gr_po:
        grid[i][j] = 1
    
    grido = grid[:]

    clock = pygame.time.Clock()

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
                    grid = [ [ 0 for _ in range(c_n)] for _ in range(r_n)]
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                press = True
            elif event.type == pygame.MOUSEBUTTONUP:
                press = False

                
            if press is True:
                pos = pygame.mouse.get_pos()
                colu = pos[0]/(WIDTH+MARGIN)
                ro = pos[1]/(HEIGHT+MARGIN)
                if rev is True:
                    print(f"[{int(colu)},{int(ro)}],", end=' ')
                    colu, ro = ro, colu
                else:
                    print(f"[{int(ro)},{int(colu)}],", end=' ')

                if grid[int(ro)][int(colu)] == 0:
                    grid[int(ro)][int(colu)] = 1
                else:
                    grid[int(ro)][int(colu)] = 0

        
        #clock.tick(speed)
        run = False
        if free is False and pau is True:
            run = True
        elif free is False and pau is False:
            pygame.time.wait(speed)
        if free is True and pau is True:
            run = True

        screen = draw(screen, grid, grid_n, r_n, c_n, MARGIN, WIDTH, HEIGHT, rev, font, dr_txt)
        if run is False:
            for r in range(r_n):
                for c in range(c_n):
                    num = check(grid, r, c)
                    grid_n[r][c] = num

            grido = grid.copy()
            for r in range(r_n):
                for c in range(c_n):
                    num = grid_n[r][c]
                    if grido[r][c] == 2:
                        grid[r][c] = 1
                    if grido[r][c] == 0 and num == b_val:
                        grid[r][c] = 2
                    if grido[r][c] != 0 and (num == s_val1 or num == s_val2):pass
                    else:
                        grid[r][c] = 0

        if free is False and step is True:
            pau = True
            step = False

        pygame.display.update()
        screen.fill(GRAY)
        co += 1

    pygame.quit()