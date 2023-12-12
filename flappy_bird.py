import random
import sys
import pygame

pygame.init()
pygame.font.init()

BG = pygame.image.load('pics/background.png')
GRAVITY = 0.25
TERMINAL_VELOCITY = 10
JUMP = -7
clock = pygame.time.Clock()

SCREEN_WIGHT, SCREEN_HEIGHT = 900, 403
WIN = pygame.display.set_mode((SCREEN_WIGHT, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

bird_wight, bird_height = 60, 60
bird_img = pygame.image.load('pics/bird.png')
bird_scaled = pygame.transform.scale(bird_img, (bird_wight, bird_height))
PIPE_WIGHT, PIPE_HEIGHT = 500, 600
pipe_img = pygame.image.load('pics/pipe.png')
pipe_scaled = pygame.transform.scale(pipe_img, (PIPE_WIGHT, PIPE_HEIGHT))


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self._img = bird_scaled
        self._rect = self._img.get_rect()
        self._rect.topleft = (x, y)
        self._mask = pygame.mask.from_surface(self._img)
        self._y = y
        self._x = x
        self._velocity = 0

    def draw(self, window):
        window.blit(self._img, (self._x, self._y))

    def gravity(self):
        self._y += self._velocity
        self._velocity = min(self._velocity + GRAVITY, TERMINAL_VELOCITY)

    def jump(self):
        self._velocity = JUMP

    def check_exit(self):
        if self._y < -50 or self._y > SCREEN_HEIGHT:
            sys.exit()


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self._img = pipe_scaled
        self._rect = self._img.get_rect()
        self._rect.topleft = (x, y)
        self._y = y
        self._x = x

    def draw(self, window):
        window.blit(self._img, (self._x, self._y))

    def move(self):
        self._x -= 5

    def pos(self):
        return self._x

    def spawn(self):
        self._x = 950 + gap
        self._y = -50 + dynamic_height


def draw_window(bird, pipes):
    WIN.blit(BG, (0, 0))
    bird.draw(WIN)
    for pipe in pipes:
        pipe.draw(WIN)
    pygame.display.flip()


bird = Bird(100, 250)
pipes = [Pipe(500, -50), Pipe(400, -50), Pipe(300, -50), Pipe(200, -50), Pipe(100, -50)]

bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

bird_group.add(bird)
for pipe in pipes:
    pipe_group.add(pipe)

running = True
while running:
    gap = random.randint(75, 200)
    dynamic_height = random.randint(-100, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    draw_window(bird, pipes)
    bird.gravity()
    bird.check_exit()
    for pipe in pipes:
        pipe.move()
        if pipe.pos() < -275:
            pipe.spawn()

    clock.tick(60)
