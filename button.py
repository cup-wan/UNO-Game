import pygame
from pygame.locals import *

pygame.init()

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 폰트 초기화
pygame.font.init()
BUTTON_FONT = pygame.font.SysFont('Arial', 24)

class Button:
    def __init__(self, x_ratio, y_ratio, width_ratio, height_ratio, text, button_color=WHITE, text_color=BLACK, y_offset=0):
        self.x_ratio = x_ratio
        self.y_ratio = y_ratio
        self.width_ratio = width_ratio
        self.height_ratio = height_ratio
        self.button_color = button_color
        self.text_color = text_color
        self.y_offset = y_offset  # 버튼 상하 위치 조절
        self.text = text
        self.text_surface = BUTTON_FONT.render(self.text, True, self.text_color)
        self.update_size()


    def update_size(self):
        screen_width, screen_height = pygame.display.get_surface().get_size()
        self.width = int(screen_width * self.width_ratio)
        self.height = int(screen_height * self.height_ratio)
        self.x = int(screen_width * self.x_ratio) - int(self.width / 2)
        self.y = int(screen_height * self.y_ratio) - int(self.height / 2) + self.y_offset  # 버튼 상하 위치 조절
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text_surface = BUTTON_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.button_color, self.rect)
        surface.blit(self.text_surface, self.text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False




######### 테스트 코드 ##########




# # 화면 초기화
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Button Test")

# # 버튼 초기화
# button = Button(0.5, 0.5, 0.2, 0.1, "Click me", y_offset=100)


# # 게임 루프
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()

#         # 화면 크기 변경 이벤트 처리
#         if event.type == pygame.VIDEORESIZE:
#             screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
#             button.update_size()

#         # 버튼 이벤트 처리
#         if button.handle_event(event):
#             print("Button clicked!")

#     # 화면 업데이트
#     screen.fill(WHITE)
#     button.draw(screen)
#     pygame.display.update()
