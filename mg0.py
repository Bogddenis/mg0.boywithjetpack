import pygame
import random


WIDTH = 480
HEIGHT = 600
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("mg0")
clock = pygame.time.Clock()
f=pygame.font.Font('PressStart2P.ttf', 10)
text=f.render("alpha0.0.2 Boy with Rocket Indev", 0, BLACK)
collide = False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 60))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT - 70
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a] or keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_d] or keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_w] or keystate[pygame.K_UP]:
            self.speedy = -8
        if not(keystate[pygame.K_w] or keystate[pygame.K_UP]):
            self.speedy = 2
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT - 10:
            self.rect.bottom = HEIGHT - 10

class Kolucka(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT - 35
        

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
kaktus = Kolucka()
all_sprites.add(kaktus)
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
            
    # Обновление
    all_sprites.update()
    # Рендеринг
    screen.fill(WHITE)
    all_sprites.draw(screen)
    screen.blit(text, (0, HEIGHT-10))
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
    if kaktus.rect.right > player.rect.left and \
       kaktus.rect.left < player.rect.right and \
       kaktus.rect.bottom > player.rect.top and \
       kaktus.rect.top < player.rect.bottom:
            collide = True
    if collide == True:
        break
pygame.quit()