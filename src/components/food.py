import pygame


class FoodState:
    RIPEN = 0
    EATEN = 1
    GROWING = 2
    SEEDED = 3


class Food:
    size = (50, 50)
    eaten_image = pygame.transform.scale(pygame.image.load('./assets/images/plantation_small.png'), size)
    seeded_image = pygame.transform.scale(pygame.image.load('./assets/images/plantation_small.png'), size)
    growing_image = pygame.transform.scale(pygame.image.load('./assets/images/plantation_medium.png'), size)
    ripen_image = pygame.transform.scale(pygame.image.load('./assets/images/plantation_large.png'), size)

    def __init__(self, pos, ecosystem, screen):
        self.pos = pos
        self.screen = screen
        self.food = pygame.Rect(self.pos, self.size)
        self.ecosystem = ecosystem

        self.state = FoodState.SEEDED
        self.time = 0

    def update(self):
        self.time += 1

        if self.state == FoodState.RIPEN:
            if self.time >= 500:
                self.ecosystem.add_food((self.pos[0] - self.size[0], self.pos[1] - self.size[1]))
                self.time = 0

        elif self.state == FoodState.SEEDED or self.state == FoodState.EATEN:
            if self.time >= 100:
                self.state = FoodState.GROWING
                self.time = 0
        elif self.state == FoodState.GROWING:
            if self.time >= 100:
                self.state = FoodState.RIPEN
                self.time = 0

    def change_state(self, state):
        self.state = state
        self.time = 0

    def draw(self):
        self.update()
        image = None

        if self.state == FoodState.SEEDED:
            image = self.seeded_image
        elif self.state == FoodState.GROWING:
            image = self.growing_image
        elif self.state == FoodState.RIPEN:
            image = self.ripen_image
        elif self.state == FoodState.EATEN:
            image = self.eaten_image

        self.screen.blit(image, self.food)
