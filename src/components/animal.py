import abc

import pygame


class Animal(abc.ABC):
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.animals = []
        self.waters = []
        self.foods = []

    @abc.abstractmethod
    def draw(self):
        pass
