import random

import pygame
from pygame.locals import RESIZABLE

from src.components.ecosystem import Ecosystem
from src.components.food import Food
from src.components.rabbit import Rabbit
from src.components.water import Water
from src.utilities.position import get_random_position

pygame.init()
pygame.font.init()
pygame.mixer.init()


def main():
    pygame.init()
    pygame.display.set_caption('Ecosystem Simulation')
    background = pygame.transform.scale(pygame.image.load('./assets/images/backgrounds/abstract_3.jpg'), (500, 500))

    display = (1200, 700)
    screen = pygame.display.set_mode(display, RESIZABLE)

    ecosystem = Ecosystem(screen)

    num_foods = 20
    for _ in range(num_foods):
        ecosystem.add_food()

    num_waters = 2
    for _ in range(num_waters):
        ecosystem.add_water()

    num_rabbits = 10
    for _ in range(num_rabbits):
        ecosystem.add_animal()

    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for y in range(0, screen.get_height(), background.get_height()):
            for x in range(0, screen.get_width(), background.get_width()):
                screen.blit(background, (x, y))

        ecosystem.draw()
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
