import pygame as pg
import pygame.display as disp
import numpy as np

pg.init()
screenwidth = 1280
screenheight = 720
screen = disp.set_mode((screenwidth, screenheight))
clock = pg.time.Clock()
running = True

board = np.zeros((10,10))

def grid(gridsize, gridamount):
    top = screenwidth / 16
    left = screenheight * 6/8 
    gridspacing = gridsize/gridamount
    for x in range(gridamount):
        for y in range(gridamount):
            gridsquare = pg.Rect(gridspacing*x + left + 5*x, gridspacing*y + top +5*y, gridspacing, gridspacing)
            if board[x][y] == 1:
                pg.draw.rect(screen, (50, 50, 100), gridsquare)
            else:    
                pg.draw.rect(screen, (50, 50, 255), gridsquare)

class Ship:
    def __init__(self, length=int, vertical=bool, start=tuple):
        self.length = length
        self.vertical = vertical
        self.start = start

    def place_ship(self):
        if self.vertical:
            for i in range(self.length):
                board[self.start[0]][self.start[1]+i] = 1
        else:
            for i in range(self.length):
                board[self.start[0]+i][self.start[1]] = 1

def ShipButton(picture, coords, surface):
    image = pg.image.load(picture)
    imagerect = image.get_rect()
    imagerect.topleft = coords
    surface.blit(image, imagerect)
    return(image, imagerect)

destroyer = Ship(5, False, (3,3))
destroyer.place_ship()                

while running:
    clock.tick(60) #60 fps

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((100, 100, 255))

    #Render

    grid(500, 10)
    destroyer_button = ShipButton('destroyer.jpg', (50, 50), screen)

    disp.flip()


pg.quit()