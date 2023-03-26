import pygame
import sys
from pygame.locals import *
import loadcard
import popup

draw_num=0;
turn = 0 #현재 턴
turn_clockwise = True #게임 진행방향 true면 turn +1 증가(시계방향)/false면 -1

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
                            self.waste_group.add(temp)                   #temp를 버리는 그룹에 추가
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
    
def result(self):
        pygame.init()
        pygame.draw.rect(self.screen, (255, 51, 0), pygame.Rect(200, 200, 400, 200))    #글자 나오는 네모칸 테두리
        pygame.draw.rect(self.screen, (255, 180, 0), pygame.Rect(210, 210, 380, 180))   #글자 나오는 네모칸 속
        
        if len(self.user_group) == 0:
            close_text = self.text_format("YOU WIN!", 'Berlin Sans FB', 80, (255,51,0)) #이기면
            press_text = self.text_format("Press SPACE to REPLAY", 'Berlin Sans FB', 35, (255,51,0))
            self.screen.blit(close_text, (230, 220))
        else:
            close_text = self.text_format("YOU LOSE!", 'Berlin Sans FB', 80, (255,51,0))#지면
            press_text = self.text_format("Press SPACE to REPLAY", 'Berlin Sans FB', 35, (255,51,0))
            self.screen.blit(close_text, (212, 220))
            
        self.screen.blit(press_text, (228, 330))
        pygame.display.update()
        
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == KEYDOWN:       
                    if event.key == K_SPACE:    #스페이스바 누르면 리겜
                        self.startgame()        #메인메뉴 가기로 해도 됨
                        return
        return 0
    
def skip(self, turn):
        if turn_clockwise == True:
            #self.player[turn+1] 사람의 손 패의 좌표를 얻고
            #그 좌표에 금지 표시 이미지 1초간 생성 후 삭제
            return
        else:
            #self.player[turn-1] 사람의 손 패의 좌표를 얻고
            #그 좌표에 금지 표시 이미지 1초간 생성 후 삭제
            return
    
def draw(self, draw_num):
        if turn_clockwise == True:
            #self.player[turn+1] 사람의 손 패의 좌표를 얻고
            #그 좌표에 +draw_num 표시 이미지 1초간 생성 후 삭제
            return
        else:
            #self.player[turn-1] 사람의 손 패의 좌표를 얻고
            #그 좌표에 +draw_num 표시 이미지 1초간 생성 후 삭제
            return
        return
        
def reverse(self, turn_clockwise):
        if turn_clockwise == True:
            img_clockwise=pygame.image.load('img_clockwise')
            img_clockwise=pygame.transform.scale(img_clockwise, (200, 200))
            self.screen.blit(img_clockwise, (200,200))#좌표, 시계방향 이미지 1초간 출력 ->
            sleep(1)
            img_clockwise.remove
            return
        else:
            img_counterclockwise=pygame.image.load('img_counterclockwise')
            img_counterclockwise=pygame.transform.scale(img_counterclockwise, (200, 200))
            self.screen.blit(img_counterclockwise, (200,200))#좌표, 반시계방향 이미지 1초간 출력
            sleep(1)
            img_counterclockwise.remove
            return
