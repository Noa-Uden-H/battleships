import pygame as pg
import pygame.display as disp

pg.init()
screenwidth = 1280
screenheight = 720
screen = disp.set_mode((screenwidth, screenheight))
clock = pg.time.Clock()
running = True

def grid(gridsize, gridamount):
    top = screenwidth / 16
    left = screenheight * 6/8 
    gridspacing = gridsize/gridamount
    for x in range(gridamount):
        for y in range(gridamount):
            gridsquare = pg.Rect(gridspacing*x + left + 5*x, gridspacing*y + top +5*y, gridspacing, gridspacing)
            pg.draw.rect(screen, (50, 50, 255), gridsquare)

while running:
    clock.tick(60) #60 fps

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((100, 100, 255))

    #Render

    grid(500, 10)

    disp.flip()


pg.quit()