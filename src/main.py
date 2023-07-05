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
    pygame.display.set_caption('Hello World!')
    background = pygame.image.load('./assets/images/backgrounds/mud-pattern.jpg')

    display = (1200, 700)
    screen = pygame.display.set_mode(display, RESIZABLE)

    ecosystem = Ecosystem(screen)

    num_foods = 10
    for _ in range(num_foods):
        ecosystem.add_food(
            Food((random.randint(0, screen.get_width()), random.randint(0, screen.get_height())), screen))

    num_waters = 4
    for _ in range(num_waters):
        ecosystem.add_water(
            Water((random.randint(0, screen.get_width()), random.randint(0, screen.get_height())), screen))

    num_rabbits = 40
    for _ in range(num_rabbits):
        random_pos = get_random_position(screen.get_size())
        rabbit = Rabbit(random_pos, screen, random.randint(0, 1), random.randint(0, 360))
        ecosystem.add_animal(rabbit)

    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        scaled_background = pygame.transform.scale(background, screen.get_size())
        screen.blit(scaled_background, (0, 0))
        ecosystem.draw()
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
