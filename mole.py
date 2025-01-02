import pygame
import random
from pygame.surface import *

class Mole:
    def __init__(self,screen:Surface):
        self.screen = screen
        self.rect = pygame.rect.Rect(0,0,125,125)
        self.mFont = pygame.font.SysFont("malgungothic", 38)
        self.mole_img = pygame.image.load('./imgs/mole.png')
        self.mole_img = pygame.transform.scale(self.mole_img , (50, 50))
        self.mole_rec = self.mole_img.get_rect()
        self.clr = (0,0,0)
        self.num_x = 0
        self.num_y = 0
        self.t_random = 0
        self.mouse_once = 0
        self.game_mode = 0
        self.hp = 5
        self.score = 0
        self.img_del = 0
        self.rect_img = None
        self.t_img = 2000

    def random_num(self):
        if self.t_random != 0:
            if (pygame.time.get_ticks() - self.t_random) > self.t_img:
                self.img_del = 0
                self.num_x = random.randint(0,2)
                self.num_y = random.randint(0,2)
                print("랜덤좌표",self.num_x , "," , self.num_y)
                self.t_random = 0
                self.t_random = pygame.time.get_ticks()
                # pygame.time.set_timer

    def text(self):
        if self.game_mode == 0:#준비
            mode_0 = self.mFont.render(f"game start: space", True, (0,0,0))
            rec_t = mode_0.get_rect()
            rec_t.centerx = self.screen.get_width()/2
            rec_t.centery = self.screen.get_height()/4
            self.screen.blit(mode_0, rec_t)

            self.screen.blit(self.mole_img,(200,300))

        if self.game_mode == 1:#시작
            mode_1 = self.mFont.render(f"hp:{self.hp},score:{self.score}", True, (0,0,255))
            rec_t = mode_1.get_rect()
            rec_t.centerx = self.screen.get_width()-130
            rec_t.centery = self.screen.get_height()/7
            self.screen.blit(mode_1, rec_t)
            
        if self.game_mode == 2:#종료
                mode_2 = self.mFont.render(f"game over // score: {self.score}", True, (255,0,0))
                rec_t = mode_2.get_rect()
                rec_t.centerx = self.screen.get_width()/2
                rec_t.centery = self.screen.get_height()/3
                self.screen.blit(mode_2, rec_t)
    
    def draw(self):
        self.text()  
        self.random_num() 
        if self.game_mode == 1:
            for i in range(3):
                for k in range(4):
                    self.rect.x = k*125
                    self.rect.y = (i+1)*125
                    # i가 0 = 125 1 = 250 , 3 = 375
                    if self.num_x == k and self.num_y == i:
                        self.mole_rec.centerx = self.rect.centerx
                        self.mole_rec.centery = self.rect.centery 
                        if self.img_del == 0:
                            self.screen.blit(self.mole_img,self.mole_rec)
                    mouse_pos = pygame.mouse.get_pos()
                    if self.rect.collidepoint(mouse_pos):
                        if self.mouse_once == 0:
                            self.clr = (255,0,0)
                        else:
                            self.clr = (0,255,0)
                        if pygame.mouse.get_pressed()[0] and self.mouse_once == 0:
                            if i == self.num_y and k == self.num_x:
                                print("정답답")
                                self.score += 1
                                self.img_del = 1
                                if self.t_img > 200:
                                    self.t_img -= 50
                            else:
                                self.hp -= 1
                                if self.hp <= 0:
                                    self.game_mode = 2
                            self.mouse_once = 1
                    else:
                        self.clr = (0,0,0)
                    if pygame.mouse.get_pressed()[0] == False:
                        self.mouse_once = 0
                    pygame.draw.rect(self.screen,self.clr,self.rect,5)

                