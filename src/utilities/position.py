import random


def get_random_position(screen_size) -> tuple:
    """Returns a random position in the screen"""
    return random.randint(0, screen_size[0]), random.randint(0, screen_size[1])
