import random
import sys
import pygame

pygame.init()
pygame.font.init()

BG = pygame.image.load('pics/background.png')
GRAVITY = 2.5
JUMP = 50

SCREEN_WIGHT, SCREEN_HEIGHT = 900, 403
WIN = pygame.display.set_mode((SCREEN_WIGHT, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

bird_wight, bird_height = 60, 60
bird_img = pygame.image.load('pics/bird.png')
bird_scaled = pygame.transform.scale(bird_img, (bird_wight, bird_height))
PIPE_WIGHT, PIPE_HEIGHT = 500, 600
pipe_img = pygame.image.load('pics/pipe.png')
pipe_scaled = pygame.transform.scale(pipe_img, (PIPE_WIGHT, PIPE_HEIGHT))


class Bird:
    def __init__(self, x, y):
        self._img = bird_scaled
        self._x = x
        self._y = y

    def draw(self, window):
        window.blit(self._img, (self._x, self._y))

    def gravity(self):
        self._y += GRAVITY

    def jump(self):
        self._y -= JUMP

    def check_exit(self):
        if self._y < -50 or self._y > 500:
            sys.exit()


class Pipe:
    def __init__(self, x, y):
        self._img = pipe_scaled
        self._x = x
        self._y = y

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
    pygame.display.update()


bird = Bird(100, 250)
pipes = [Pipe(500, -50), Pipe(400, -50), Pipe(300, -50), Pipe(200, -50), Pipe(100, -50)]

running = True
while running:
    gap = random.randint(-200, 200)
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



"""
fix bug with pipes
change gravity
"""
