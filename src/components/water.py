import pygame


class WaterState:
    FULL = 0
    EMPTY = 1
    FILLING = 2


class Water:
    size = (100, 100)

    def __init__(self, pos, screen):
        self.pos = pos
        self.screen = screen
        self.water = pygame.Rect(self.pos, self.size)

        self.state = WaterState.EMPTY
        self.time = 0

    def update(self):
        self.time += 1

        if self.state == WaterState.EMPTY:
            if self.time >= 100:
                self.state = WaterState.FILLING
                self.time = 0
        elif self.state == WaterState.FILLING:
            if self.time >= 100:
                self.state = WaterState.FULL
                self.time = 0

    def change_state(self, state):
        self.state = state
        self.time = 0

    def draw(self):
        self.update()
        color = (0, 0, 255)
        # use different shades of blue to represent the water level
        if self.state == WaterState.EMPTY:
            color = (0, 0, 0)
        elif self.state == WaterState.FILLING:
            color = (0, 0, 200)
        elif self.state == WaterState.FULL:
            color = (0, 0, 255)

        pygame.draw.rect(self.screen, color, self.water)
