import pygame
import pygame as pg

pygame.init()


clock = pygame.time.Clock()
 

WIDTH = 480
HEIGHT = 540
FPS = 60
CAPTION = "EDT"
CYAN    = (0, 255, 255)
BLACK   = (0, 0, 0)

WINDOW = pg.display
WINDOW.set_caption(CAPTION)
SCREEN = WINDOW.set_mode((WIDTH,HEIGHT))

mine = pg.image.load("mine.png").convert_alpha()
sweeper = pg.image.load("sweeper.jpg").convert_alpha()

# 시간 정보
total_time = 90
start_ticks = pygame.time.get_ticks()

# 폰트 설정
game_font = pygame.font.Font(None, 40)

class Mob:
    def __init__(self,Hp,Armor,Speed,Reward,Tier,Attack):
        self.Hp = Hp
        self.Armor = Armor
        self.Speed = Speed
        self.Reward = Reward
        self.Tier = Tier
        self.Attack = Attack
        self.mob_Rect = None
        # self.pos = 


    # 이미지가 원하는 위치에 올 수 있도록 좌표값 수정
    def Rect(self):
        if self.Tier == 1:
            self.mob_Rect = mine.get_rect()
            self.mob_Rect.centerx = 15
            self.mob_Rect.centery = 540
        
        elif self.Tier == 2:
            self.mob_Rect = mine.get_rect()
            self.mob_Rect.centerx = 100
            self.mob_Rect.centery = 540

    #몹을 움직이게 함
    def Move(self):
        if self.Tier == 1:
            # 스크린의 원하는 좌표에 이미지 복사하기, 좌표값은 Rect를 이용
            SCREEN.blit(mine, self.mob_Rect)
            # 이미지의 y 좌표값을 감소
            if self.mob_Rect.y >= 400:
                self.mob_Rect.y -= self.Speed

            elif self.mob_Rect.y <= 400:
                self.mob_Rect.x += self.Speed
                
                if self.mob_Rect.x >= 100:
                    self.mob_Rect.y -= self.Speed
                    self.mob_Rect.x -= self.Speed

        elif self.Tier == 2:
            SCREEN.blit(mine, self.mob_Rect)
            if self.mob_Rect.y >= 400:
                self.mob_Rect.y -= self.Speed

            elif self.mob_Rect.y <= 450:
                self.mob_Rect.x += self.Speed
                
                if self.mob_Rect.x >= 300:
                    self.mob_Rect.x -= self.Speed
                    self.mob_Rect.y -= self.Speed



# class Round:
#     def __init__(self):




mob1 = Mob(10,1,1,5,1,1)
mob2 = Mob(10,1,2,5,2,1)
mob1.Rect()
mob2.Rect()


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pg.QUIT:
            running = False

    SCREEN.fill(BLACK)

    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    if elapsed_time >= 0:
        mob1.Move()

    if elapsed_time >= 3:
        mob2.Move()


    # 타이머
    timer = game_font.render("timer: " + str(int(total_time - elapsed_time)), True, (255,255,255))

    #경과 시간 표시
    SCREEN.blit(timer, (240, 10))


    pygame.display.update()