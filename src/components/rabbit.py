import random

import pygame
import numpy as np

from src.components.animal import Animal
from src.components.food import FoodState
from src.components.water import WaterState


class RabbitState:
    SLEEPING = 0
    EATING = 1
    DRINKING = 2
    MATING = 3
    IDLE = 4
    JUMPING = 5


class Rabbit(Animal):
    size = (20, 20)
    threshold = 500

    def __init__(self, pos: tuple, screen: pygame.Surface, sex: int, direction: int = 0):
        super().__init__(screen)
        self.rabbit = pygame.Rect(pos, self.size)
        self.pos = pos
        self.screen = screen

        self.foods = []
        self.waters = []
        self.animals = []

        self.sex = sex
        # use colors yellow and pink based on sex, Females are pink, Males are blue
        self.color = (0, 0, 255) if self.sex else (255, 0, 255)

        self.hunger = 0
        self.thirst = 0
        self.tiredness = 0
        self.happiness = 0
        self.reproductive_urge = 0
        self.age = 0
        self.alive = True

        self.state = RabbitState.IDLE
        self.direction = direction
        self.jump_distance = 2
        self.time = 0

    def move(self):
        self.pos = (self.pos[0] + self.jump_distance * np.cos(self.direction),
                    self.pos[1] + self.jump_distance * np.sin(self.direction))

        if self.pos[0] < 0:
            self.pos = (0, self.pos[1])
        elif self.pos[0] > self.screen.get_width() - self.size[0]:
            self.pos = (self.screen.get_width() - self.size[0], self.pos[1])

        if self.pos[1] < 0:
            self.pos = (self.pos[0], 0)
        elif self.pos[1] > self.screen.get_height() - self.size[1]:
            self.pos = (self.pos[0], self.screen.get_height() - self.size[1])

        self.rabbit = pygame.Rect(self.pos, self.size)

    def update(self):
        self.hunger += 1
        self.thirst += 1
        self.tiredness += 1
        self.happiness += 1
        self.reproductive_urge += 1

    def find_nearest_resource(self, resources):
        """Finds the closest resource in resources"""
        if not resources:
            random_position = random.randint(0, self.screen.get_width()), random.randint(0, self.screen.get_height())
            self.direction = np.arctan2(random_position[1] - self.pos[1], random_position[0] - self.pos[0])
            return

        closest_resource = np.argmin(np.linalg.norm(np.array(resources) - np.array(self.pos), axis=1))
        self.direction = np.arctan2(resources[closest_resource][1] - self.pos[1],
                                    resources[closest_resource][0] - self.pos[0])

    def control(self):
        self.time += 1
        self.update()

        if self.state == RabbitState.IDLE:
            self.handle_collision_with_food()
            self.handle_collision_with_water()
            self.handle_collision_with_mate()
            self.handle_idleness()

        elif self.state == RabbitState.EATING:
            self.handle_eating()
        elif self.state == RabbitState.DRINKING:
            self.handle_drinking()
        elif self.state == RabbitState.MATING:
            self.handle_mating()
        elif self.state == RabbitState.SLEEPING:
            self.handle_sleeping()

        self.move()

    def handle_idleness(self):
        priority = max([self.hunger, self.thirst, self.reproductive_urge])
        if self.hunger == priority:
            if self.hunger > 3 * self.threshold:
                print('Dead because of hunger')
                self.alive = False
            if self.hunger > self.threshold:
                food_pos = [food.pos for food in self.foods if food.state == FoodState.RIPEN]
                self.find_nearest_resource(food_pos)

        elif self.thirst == priority:
            if self.thirst > 3 * self.threshold:
                print('Dead because of thirst')
                self.alive = False
            if self.thirst > self.threshold:
                water_pos = [water.pos for water in self.waters]
                self.find_nearest_resource(water_pos)

        elif self.reproductive_urge == priority:
            if self.reproductive_urge > 5 * self.threshold:
                print('Dead because of reproductive urge')
                self.alive = False

            if self.reproductive_urge > self.threshold and self.sex:
                mates_pos = [mate.pos for mate in self.animals if
                             (mate.state != RabbitState.MATING and mate.sex == 1 - self.sex)]
                self.find_nearest_resource(mates_pos)

    def handle_eating(self):
        if self.time > 50:
            self.jump_distance = 2
            self.state = RabbitState.IDLE

    def handle_drinking(self):
        if self.time > 50:
            self.jump_distance = 2
            self.state = RabbitState.IDLE

    def handle_mating(self):
        if self.time > 50:
            self.jump_distance = 2
            self.state = RabbitState.IDLE

    def handle_sleeping(self):
        pass

    def handle_collision_with_food(self):
        for food in self.foods:
            if food.state == FoodState.RIPEN and self.rabbit.colliderect(food.food):
                self.eat()
                food.change_state(FoodState.EATEN)

    def handle_collision_with_mate(self):
        for animal in self.animals:
            if type(animal) == Rabbit and animal.sex == 1 - self.sex:
                rabbit = animal

                if rabbit.rabbit.colliderect(self.rabbit) and rabbit.state != RabbitState.MATING \
                        and rabbit.reproductive_urge > 3 * self.threshold and self.reproductive_urge > self.threshold:
                    self.mate()
                    rabbit.mate()

    def handle_collision_with_water(self):
        for water in self.waters:
            if water.state == WaterState.FULL and self.rabbit.colliderect(water.water):
                self.drink()
                water.change_state(WaterState.EMPTY)

    def age(self):
        self.age += 1
        self.time = 0

    def eat(self):
        self.jump_distance = 0
        self.state = RabbitState.EATING
        self.hunger = 0
        self.time = 0

    def drink(self):
        self.jump_distance = 0
        self.state = RabbitState.DRINKING
        self.thirst = 0
        self.time = 0

    def mate(self):
        self.jump_distance = 0
        self.state = RabbitState.MATING
        self.reproductive_urge = 0
        self.time = 0

    def die(self):
        self.state = RabbitState.IDLE
        self.alive = False

    def sleep(self):
        self.state = RabbitState.SLEEPING
        self.tiredness = 0

    def jump(self):
        self.state = RabbitState.JUMPING
        self.happiness = 0

    def draw(self):
        if self.alive:
            pygame.draw.rect(self.screen, self.color, self.rabbit)
