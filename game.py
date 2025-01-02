
import pygame
from mole import*

class Game:
    is_run = True
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500,500))
        self.clock = pygame.time.Clock() #프레임을 처리 하기위해
        self.mole = Mole(self.screen)
    
    def eventprocess(self):
        for event in pygame.event.get():#이벤트 가져오기
            if event.type == pygame.QUIT: #종료버튼?
                self.is_run = False
            if event.type == pygame.KEYDOWN:#키 눌림?
                if event.key == pygame.K_SPACE:
                    if self.mole.game_mode == 0:
                        self.mole.game_mode = 1
                        self.mole.t_random = pygame.time.get_ticks()

                    if self.mole.game_mode == 2:
                        self.mole.num_x = 0
                        self.mole.num_y = 0
                        self.mole.t_random = 0
                        self.mole.mouse_once = 0
                        self.mole.game_mode = 0
                        self.mole.hp = 5
                        self.mole.score = 0
                        self.mole.t_img = 2000

    def run(self):
        while self.is_run:
            self.screen.fill((255,255,255))
            self.eventprocess()
            self.mole.draw()
            pygame.display.update()
            self.clock.tick(60)



game = Game()
game.run()

