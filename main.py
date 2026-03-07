import pygame


class Sprite:
    def __init__(self, center, image):
        self.image = image
        self.rect = self.image.get_frect()
        self.rect.center = center

    def render(self, surface):
        surface.blit(self, image, self.rect)

class MoveSprite(Sprite):
    def __init__(self, center, image, speed, direction):
        super().__init__(center, image)

        self.speed = speed
        self.direction = direction.normalize()

    def update(self):
        vector = self.direction * self.speed
        self.rect.move_ip(vector)



WINDOW_SIZE = (800, 600)
MAX_FPS = 60

window = pygame.Window('Towel Defense', WINDOW_SIZE)
surface = window.get_surface()

clock = pygame.Clock()

center = WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2
image = pygame.Surface((50, 50))
image.fill('red')
player = Sprite(center, image)

running = True

while running:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False

    #

    #
    surface.fill('white')
    player.render(surface)
    window.flip()

    clock.tick(MAX_FPS)
    print(clock.get_fps())