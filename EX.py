import popup
import pygame
from pygame.locals import *
import loadcard

def pick_color(self):                                                    #색 고르는 스킬 팝업 생성
        color_popup = popup.Popup('pickcolor', (400, 300))
        popup_group = pygame.sprite.RenderPlain(color_popup)             #그룹을 만든다
        red = popup.Popup('RED', (306, 320))                             #name이 RED로 되어 RED이미지 불러옴,숫자는 좌표
        yellow = popup.Popup('YELLOW', (368, 320))
        green = popup.Popup('GREEN', (432, 320))
        blue = popup.Popup('BLUE', (494, 320))
        colors = [red, yellow, green, blue]
        color_group = pygame.sprite.RenderPlain(*colors)

        loop = True
        while loop:
            popup_group.draw(self.screen)
            color_group.draw(self.screen)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    for sprite in color_group:
                        if sprite.get_rect().collidepoint(mouse_pos):    #색 클릭 판단
                            temp_name = sprite.get_name()                #클릭된 것의 이름을 임시로 저장
                            temp = loadcard.Card(temp_name, (430, 300))  #카드를 정해진 좌표로 불러옴(버린 카드 모아둔 곳 좌표)
                            self.waste_card.append(temp_name)            
                            self.waste_group.add(temp)                   #temp를 버리는 sprite 그룹에 추가
                            self.printwindow()
                            loop = False

                if event.type == KEYDOWN:                                #키보드  
                    if event.key == K_LEFT:                                   
                        if selected <=1:
                            selected = 1
                        else:
                            selected = selected-1
                    elif event.key == K_RIGHT:
                        if selected >=4:
                            selected = 4
                        else:
                            selected = selected+1
                    if event.key == K_RETURN:
                        if selected <= 1:
                            temp = loadcard.Card('RED', (430, 300))
                            self.waste_group.add(temp)
                            self.printwindow()
                            loop = False
                        if selected == 2:
                            temp = loadcard.Card('YELLOW', (430, 300))
                            self.waste_group.add(temp)
                            self.printwindow()
                            loop = False
                        if selected == 3:
                            temp = loadcard.Card('GREEN', (430, 300))
                            self.waste_group.add(temp)
                            self.printwindow()
                            loop = False
                        if selected >= 4:
                            temp = loadcard.Card('BLUE', (430, 300))
                            self.waste_group.add(temp)
                            self.printwindow()
                            loop = False 
        return 0
    
def 
