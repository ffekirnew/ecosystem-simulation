import random

import pygame

from src.components.food import Food
from src.components.rabbit import Rabbit
from src.components.water import Water


class Ecosystem:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.foods = []
        self.waters = []
        self.animals = []

    def add_food(self, pos=None):
        if not pos:
            pos = (random.randint(0, self.screen.get_width() - Food.size[0]),
                   random.randint(0, self.screen.get_height() - Food.size[1]))
        food = Food(pos, self, self.screen)
        self.foods.append(food)

    def add_water(self, pos=None):
        if not pos:
            pos = (random.randint(0, self.screen.get_width() - Water.size[0]),
                   random.randint(0, self.screen.get_height() - Water.size[1]))
        water = Water(pos, self.screen)
        self.waters.append(water)

    def add_animal(self, pos=None, sex=None):
        if not pos:
            pos = (random.randint(0, self.screen.get_width() - Rabbit.size[0]),
                   random.randint(0, self.screen.get_height() - Rabbit.size[1]))
        if not sex:
            sex = random.randint(0, 1)

        animal = Rabbit(pos, self.screen, sex, random.randint(0, 360))
        self.animals.append(animal)

        animal.animals = self.animals
        animal.waters = self.waters
        animal.foods = self.foods

    def draw(self):
        for food in self.foods:
            food.draw()

        for water in self.waters:
            water.draw()

        for animal in self.animals:
            animal.control()
            animal.draw()
