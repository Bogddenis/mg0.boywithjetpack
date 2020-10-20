import pygame


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
ORANGE = (255, 132, 0)

fon = pygame.image.load('assets/fon.png')
kaktuspng = pygame.image.load('assets/kaktus.png')
longkaktuspng = pygame.image.load('assets/longkaktus.png')
blockpng = pygame.image.load('assets/block.png')
john1 = pygame.image.load('assets/John/john1.png')
john2 = pygame.image.load('assets/John/john2.png')
finishpng = pygame.image.load('assets/finish.png')
icon = pygame.image.load('assets/icon.png')
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boy with Jetpack")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
f=pygame.font.Font('PressStart2P.ttf', 10)
text=f.render("alpha0.0.5 Boy with Jetpack PROTOTYPE", 0, WHITE)
collide1 = False
collide2 = False
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = john1
        self.image.set_colorkey(WHITE)
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
            self.image = john1
            self.image.set_colorkey(WHITE)
        if keystate[pygame.K_d] or keystate[pygame.K_RIGHT]:
            self.speedx = 8
            self.image = john2
            self.image.set_colorkey(WHITE)
        if keystate[pygame.K_w] or keystate[pygame.K_UP]:
            self.speedy = -8
        if not(keystate[pygame.K_w] or keystate[pygame.K_UP]):
            self.speedy = 2
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (block.rect.top == self.rect.y + 60) and (240 > self.rect.x) :
            self.rect.bottom = block.rect.top - 2
        if (block.rect.top < self.rect.y + 60) and (240 < self.rect.x):
            self.speedy = -2
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
        if kaktus.rect.right > player.rect.left and \
           kaktus.rect.left < player.rect.right and \
           kaktus.rect.bottom > player.rect.top and \
           kaktus.rect.top < player.rect.bottom:
               self.rect.x = WIDTH / 2
               self.rect.y = HEIGHT - 70
        if longkaktus1.rect.right > player.rect.left and \
           longkaktus1.rect.left < player.rect.right and \
           longkaktus1.rect.bottom > player.rect.top and \
           longkaktus1.rect.top < player.rect.bottom:
               self.rect.x = WIDTH / 2
               self.rect.y = HEIGHT - 70
        if longkaktus2.rect.right > player.rect.left and \
           longkaktus2.rect.left < player.rect.right and \
           longkaktus2.rect.bottom > player.rect.top and \
           longkaktus2.rect.top < player.rect.bottom:
               self.rect.x = WIDTH / 2
               self.rect.y = HEIGHT - 70


class Kolucka(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = kaktuspng
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 230
        self.rect.y = HEIGHT - 500

class polka(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = blockpng
        self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT - 250

class finish(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = finishpng
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2 + 15
        self.rect.y = HEIGHT - 500

class longKolucka1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = longkaktuspng
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2 -10
        self.rect.y = HEIGHT - 480

class longKolucka2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = longkaktuspng
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - 290
        self.rect.y = HEIGHT - 380
        self.speedx = 2
    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.speedx = -4
        if self.rect.left < 0:
            self.speedx = 4


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
kaktus = Kolucka()
all_sprites.add(kaktus)
block = polka()
all_sprites.add(block)
finish = finish()
all_sprites.add(finish)
longkaktus1 = longKolucka1()
all_sprites.add(longkaktus1)
longkaktus2 = longKolucka2()
all_sprites.add(longkaktus2)
# Цикл игры
running = True
while running:
    global self
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
    screen.blit(fon, (0, 0))
    all_sprites.draw(screen)
    screen.blit(text, (0, HEIGHT-10))
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
    if (finish.rect.top == player.rect.y + 60) and (240 < player.rect.x):
        break

pygame.quit()
