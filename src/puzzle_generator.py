# -*-coding: utf-8 -*-

import random
from itertools import product


def generate_puzzle(image, piece_size):
    width, height = image.size
    width_steps = range(0, width, piece_size)
    height_steps = range(0, height, piece_size)
    boxes = ((i, j, i+piece_size, j+piece_size)
             for i, j in product(width_steps, height_steps))

    pieces = [image.crop(box) for box in boxes]
    random.shuffle(pieces)

    return pieces, len(width_steps), len(height_steps)