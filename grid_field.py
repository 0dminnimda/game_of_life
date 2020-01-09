import pygame
 
def draw(screen, grid, r_n, c_n, MARGIN, WIDTH, HEIGHT, rev):
    if rev is True:
        c_n, r_n = r_n, c_n
    for row in range(r_n):
        for column in range(c_n):
            color = WHITE
            if rev is False and grid[row][column] == 1:
                color = GREEN
            elif rev is True and grid[column][row] == 1:
                color = GREEN
            pygame.draw.rect(screen, color, [(MARGIN+WIDTH)*column+MARGIN, (MARGIN+HEIGHT)*row+MARGIN, WIDTH, HEIGHT])
     
        
    return screen
 
def check(grid, r, c):
    grido = grid[:]
    num = 0
    for ri in range(-1,2):
        for ci in range(-1,2):
            if ri == 0 and ci == 0:pass
            else:
                try:
                    if grido[r+ri][c+ci] == 1:
                        num += 1
                    if __name__ != "__main__": 
                        print(grido[r+ri][c+ci])
                except Exception:pass
    return num

if __name__ == "__main__":
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    
    rev = bool( 0 )
    
    b_val = 3
    s_val1 = 3
    s_val2 = 5
    
    MARGIN = 2
     
    pygame.init()
     
    WINDOW_SIZE = (1540, 801) #(2340, 1080)
    #WINDOW_SIZE = WINDOW_SIZE[::-1]
    #print(WINDOW_SIZE)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    
    WIDTH = 100*0.75
    HEIGHT = 100*0.75
    
    c_n = int(WINDOW_SIZE[0]/WIDTH)
    r_n = int(WINDOW_SIZE[1]/HEIGHT)
    print(c_n, r_n)
    
    if rev is True:
        c_n, r_n = r_n, c_n
        
    grid = [ [ 0 for _ in range(c_n)] for _ in range(r_n)]
    
    pygame.display.set_caption("Array Backed Grid")
    
    done = False
    press = False
    co = 0
    
    grid[1][0] = 1
    grid[1][1] = 1
    grid[1][2] = 1
    grid[3][0] = 1
    grid[3][1] = 1
    grid[3][2] = 1
    grid[2][2] = 1
    grid[2][3] = 1
    
    clock = pygame.time.Clock()
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
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
     
        clock.tick(1)
        screen = draw(screen, grid, r_n, c_n, MARGIN, WIDTH, HEIGHT, rev)
        for r in range(r_n):
            for c in range(c_n):
                num = check(grid, r, c)
                if grid[r][c] == 0 and num == b_val:
                    grid[r][c] = 1
                if grid[r][c] == 1 and (num == s_val1 or num == s_val2):pass
                else:
                    grid[r][c] = 0
        
        pygame.display.update()
        screen.fill(BLACK)
            
        co += 1
    
    pygame.quit()