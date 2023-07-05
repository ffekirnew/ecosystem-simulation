import pygame


class Ecosystem:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.foods = []
        self.waters = []
        self.animals = []

    def add_food(self, food):
        self.foods.append(food)

    def add_water(self, water):
        self.waters.append(water)

    def add_animal(self, animal):
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
