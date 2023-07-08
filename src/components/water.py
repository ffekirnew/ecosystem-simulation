import pygame


class WaterState:
    FULL = 0
    EMPTY = 1
    FILLING = 2


class Water:
    size = (150, 150)
    water_image = pygame.transform.scale(pygame.image.load('./assets/images/water_pond_2.png'), size)

    def __init__(self, pos, screen):
        self.pos = pos
        self.screen = screen
        self.water = pygame.Rect(self.pos, self.size)

        self.state = WaterState.FULL
        self.time = 0

    def update(self):
        self.time += 1

        if self.state == WaterState.EMPTY:
            if self.time >= 0:
                self.state = WaterState.FILLING
                self.time = 0
        elif self.state == WaterState.FILLING:
            if self.time >= 0:
                self.state = WaterState.FULL
                self.time = 0

    def change_state(self, state):
        self.state = state
        self.state = WaterState.FULL
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

        self.screen.blit(self.water_image, self.water)
