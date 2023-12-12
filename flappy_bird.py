import random
import sys
import pygame

pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 36)

BG = pygame.image.load('pics/background.png')
GRAVITY = 0.25
TERMINAL_VELOCITY = 10
JUMP = -7
clock = pygame.time.Clock()
score = 0

# creates screen and caption
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 403
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')
pygame.display.set_icon(pygame.image.load('pics/epic_sax_guy.jpeg '))

# loaded images and scaled it
bird_wight, bird_height = 60, 60
bird_img = pygame.image.load('pics/bird.png')
bird_scaled = pygame.transform.scale(bird_img, (bird_wight, bird_height))
PIPE_WIGHT, PIPE_HEIGHT = 500, 600
pipe_img = pygame.image.load('pics/pipe.png')
pipe_scaled = pygame.transform.scale(pipe_img, (PIPE_WIGHT, PIPE_HEIGHT))


class Bird(pygame.sprite.Sprite):
    """
    class to for the bird and its behaviour
    :param x
    :param y
    """
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self._image = bird_scaled
        self._rect = self._image.get_rect()
        self._rect.topleft = (x, y)
        self._mask = pygame.mask.from_surface(self._image)
        self._y = y
        self._x = x
        self._velocity = 0

    @property
    def rect(self):
        return self._rect

    @property
    def image(self):
        return self._image

    def draw(self, window):
        window.blit(self._image, (self._x, self._y))

    def gravity(self):
        self._y += self._velocity
        self._velocity = min(self._velocity + GRAVITY, TERMINAL_VELOCITY)
        self._rect.y = self._y

    def jump(self):
        self._velocity = JUMP

    def check_exit(self):
        if self._y < -50 or self._y > SCREEN_HEIGHT:
            pygame.quit()
            sys.exit()

    def pos(self):
        return self._rect.x, self._rect.y


class Pipe(pygame.sprite.Sprite):
    """
    class to for the pipes and there behaviour
    :param x
    :param y
    """
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self._image = pipe_scaled
        self._rect = self._image.get_rect()
        self._rect.topleft = (x, y)
        self._mask = pygame.mask.from_surface(self._image)
        self._y = y
        self._x = x

    @property
    def rect(self):
        return self._rect

    @property
    def image(self):
        return self._image

    def draw(self, window):
        window.blit(self._image, (self._x, self._y))

    def move(self):
        self._x -= 5
        self._rect.x = self._x

    def pos(self):
        return self._x

    def check_pos(self):
        return self._rect.x, self._rect.y

    def spawn(self):
        self._x = 950 + gap
        self._y = -50 + dynamic_height
        self._rect.x = 950 + gap
        self._rect.y = -50 + dynamic_height


def draw_window(bird, pipes):
    WIN.blit(BG, (0, 0))
    bird.draw(WIN)
    for pipe in pipes:
        pipe.draw(WIN)
    WIN.blit(score_text, (10, 10))
    pygame.display.flip()


# create objects
bird = Bird(100, 250)
pipes = [Pipe(500, -50), Pipe(400, -50), Pipe(300, -50), Pipe(200, -50), Pipe(100, -50)]

# create sprite groups
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

# add objects to groups
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

    # renders score
    """score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    score += 1"""

    draw_window(bird, pipes)
    bird.gravity()
    bird.check_exit()
    for pipe in pipes:
        pipe.move()
        if pipe.pos() < -275:
            pipe.spawn()

    # collision
    if pygame.sprite.spritecollide(bird, pipe_group, False, pygame.sprite.collide_mask):
        print('You lost!')
        print(f'Your Score: {score}')
        pygame.quit()
        sys.exit()
    clock.tick(60)
