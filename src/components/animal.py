import abc

import pygame


class AnimalState:
    SLEEPING = 0
    EATING = 1
    DRINKING = 2
    MATING = 3
    IDLE = 4
    JUMPING = 5
    ALIVE = 6
    DEAD = 7


class Animal(abc.ABC):
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.animals = []
        self.waters = []
        self.foods = []

    @abc.abstractmethod
    def draw(self):
        pass
