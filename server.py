from re import I
import pygame
import pygame as pg
from datetime import timedelta
from datetime import datetime

#import module files
import element
import mob
import storeinventory
import tower

pg.init()

mine = pg.image.load("mine.png")
sweeper = pg.image.load("sweeper.jpg")
towericon = pg.image.load("tower.png")

WIDTH = 1024
HEIGHT = 576
FPS = 60
CAPTION = "ETD"
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW = pg.display
WINDOW.set_caption(CAPTION)
SCREEN = WINDOW.set_mode((WIDTH,HEIGHT))



gameFont = pygame.font.Font(None, 40)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pg.QUIT:
            running = False

    SCREEN.fill(BLACK)
    pg.draw.rect(SCREEN, WHITE, [774, 0, 300, 576])

    for i in range(1,mob.population+1):
        if timedelta(seconds = i-1) <= datetime.now() - mob.atk_time:
            mob.mobMaster[i-1].move()


    pg.time.Clock().tick(FPS)


    mob.start()
    mob.spawn()
    
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - mob.start_ticks) / 1000

    # 타이머
    timer = gameFont.render("time: " + str(int(mob.totalTime-elapsed_time)), True, (255,255,255))

    #경과 시간 표시
    SCREEN.blit(timer, (240, 10))

    pg.display.update()


