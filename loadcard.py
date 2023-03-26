import pygame
from pygame.locals import *

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
        x, y = self.position                 #현재위치
        i_x = de_pos[0]                      #목적지 위치
        i_y = de_pos[1] 
        
        movement_speed=1
        moving = True

        while moving:
             for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                       moving = False
             if x < i_x:
                  x += movement_speed
             elif x > i_x:
                  x -= movement_speed
    
             if y < i_y:
                  y += movement_speed
             elif y > i_y:
                  y -= movement_speed

             screen.fill(backgorund)          #카드 이동할 때 배경화면도 계속 최신화해야지 카드 잔상이 안보임
             screen.blit(self.image, (x, y))  #카드 움직일 때마다 이미지 생성
             pygame.display.update()

             if x == i_x and y == i_y:          
                  moving = False

        self.position = (x, y)                    
        self.rect = self.image.get_rect()      
        self.rect.center = self.position
        
        def get_rect(self):
            return self.rect
        
        def get_name(self):
            return self.name