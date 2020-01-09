import pygame
from pygame.locals import *
import numpy as np

def draw(screen, font, grid, grid_n, r_n, c_n, MARGIN, WIDTH, HEIGHT, rev):
    if rev is True:
        c_n, r_n = r_n, c_n
    for row in range(r_n):
        for column in range(c_n):
            color = WHITE
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

            text = font.render(str(grn), 1, (0, 0, 0))
            pygame.draw.rect(screen, color, [(MARGIN+WIDTH)*column+MARGIN, (MARGIN+HEIGHT)*row+MARGIN, WIDTH, HEIGHT])
            screen.blit(text, ((MARGIN+WIDTH)*column+MARGIN, (MARGIN+HEIGHT)*row+MARGIN))
     
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
    
    rev = bool( 1 )

    b_val = 3
    s_val1 = 2
    s_val2 = 3
    
    MARGIN = 2
     
    pygame.init()
     
    WINDOW_SIZE = (1540, 801) #(2340, 1080)
    #WINDOW_SIZE = WINDOW_SIZE[::-1]
    screen = pygame.display.set_mode(WINDOW_SIZE, RESIZABLE)
    
    WIDTH = 100*0.5
    HEIGHT = 100*0.5
    
    c_n = int(WINDOW_SIZE[0]/WIDTH)
    r_n = int(WINDOW_SIZE[1]/HEIGHT)
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
    co = 0
    speed = 10
    
    grid[2][1] = 1
    grid[3][2] = 1
    grid[1][3] = 1
    grid[2][3] = 1
    grid[3][3] = 1
    
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
                    speed += 1
                if event.key == K_s:
                    speed -= 1
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
                ro = pos[1] / (HEIGHT + MARGIN)
                #print("Click ", pos, "Grid coordinates: ", int(ro), int(colu))
                grid[int(colu)][int(ro)] = 1

        
        #clock.tick(speed)
        screen = draw(screen, font, grid, grid_n, r_n, c_n, MARGIN, WIDTH, HEIGHT, rev)
        if pau is False:
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
        screen.fill(BLACK)
        co += 1

    pygame.quit()