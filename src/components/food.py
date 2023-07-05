import pygame

from src.components.ecosystem import Ecosystem


class FoodState:
    RIPEN = 0
    EATEN = 1
    GROWING = 2
    SEEDED = 3


class Food:
    size = (20, 20)

    def __init__(self, pos, screen):
        self.pos = pos
        self.screen = screen
        self.food = pygame.Rect(self.pos, self.size)

        self.state = FoodState.SEEDED
        self.time = 0

    def update(self):
        self.time += 1

        if self.state == FoodState.SEEDED or self.state == FoodState.EATEN:
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
        color = (0, 255, 0)

        if self.state == FoodState.SEEDED:
            color = (0, 255, 0)
        elif self.state == FoodState.GROWING:
            color = (0, 255, 0)
        elif self.state == FoodState.RIPEN:
            color = (255, 255, 0)
        elif self.state == FoodState.EATEN:
            color = (0, 0, 0)

        pygame.draw.rect(self.screen, color, self.food)
