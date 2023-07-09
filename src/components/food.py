import math

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

        self.children = 0
        self.max_children = 4
        self.degree = 360 // self.max_children

        self.state = FoodState.SEEDED
        self.time = 0

    def update(self):
        self.time += 1

        if self.state == FoodState.RIPEN:
            if self.time >= 500 and self.children < self.max_children:
                # distribute the 10 children in circle from the original food
                center = (self.pos[0] + self.size[0] // 2, self.pos[1] + self.size[1] // 2,)
                # calculate the position of the child

                child_degree = self.children * self.degree
                child_x = center[0] + 100 * math.cos(math.radians(child_degree))
                child_y = center[1] + 100 * math.sin(math.radians(child_degree))

                self.ecosystem.add_food((child_x, child_y))
                self.time = 0
                self.children += 1

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
