import pygame
from pygame.locals import *

clock = pygame.time.Clock() #fps

class Card(pygame.sprite.Sprite):          #카드 이미지를 위한 객
    def __init__(self, name, position):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.image.load('./img/'+name+'.png')
        self.image = pygame.transform.scale(self.image, (80, 100))
        self.orig_pos = position
        self.position = position
        self.user_rotation = 30
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        
    def get_rect(self):
        return self.rect

    def get_name(self):
        return self.name

    def move(self, de_pos):
        i_x = de_pos[0]                      #목적지 위치
        i_y = de_pos[1] 
        
        movement_speed=1
        moving = True

        while moving:
             for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                       moving = False
             if self.rect.centerx < i_x:
                  self.rect.centerx += movement_speed
             elif self.rect.centerx > i_x:
                  self.rect.centerx -= movement_speed
    
             if self.rect.centery < i_y:
                  self.rect.centery += movement_speed
             elif self.rect.centery > i_y:
                  self.rect.centery -= movement_speed

             screen.fill(backgorund)          #카드 이동할 때 배경화면도 계속 최신화해야지 카드 잔상이 안보임
             screen.blit(self.image, self.rect) #이미지 복사하기, 좌표값은 rect를 이용
             pygame.display.update()

             if self.rect.centerx == i_x and self.rect.centery == i_y:          
                  moving = False
                  
             clock.tick(60)# 1초에 60번 순환
                                
        self.rect = self.image.get_rect()      
        self.rect.center = self.position
        
        def get_rect(self):
            return self.rect
        
        def get_name(self):
            return self.name
