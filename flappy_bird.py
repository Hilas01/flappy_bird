import pygame

pygame.init()
pygame.font.init()

BG = pygame.image.load('pics/background.png')
GRAVITY = 2.5
JUMP = 10
clock = pygame.time.Clock()

SCREEN_WIGHT, SCREEN_HEIGHT = 900, 504
WIN = pygame.display.set_mode((SCREEN_WIGHT, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

bird_wight, bird_height = 75, 75
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
        pass


class Pipe:
    def __init__(self, x, y):
        self._img = pipe_scaled
        self._x = x
        self._y = y

    def draw(self, window):
        window.blit(self._img, (self._x, self._y))


def draw_window(bird, pipe):
    WIN.blit(BG, (0, 0))
    bird.draw(WIN)
    pipe.draw(WIN)
    pygame.display.update()


bird = Bird(100, 250)
pipe = Pipe(500, -50)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_window(bird, pipe)
    bird.gravity()

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        bird.jump()

    clock.tick(60)
