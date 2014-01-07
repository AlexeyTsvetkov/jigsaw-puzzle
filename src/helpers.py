#!/usr/bin/python
# -*-coding: utf-8 -*-

import os

from PIL import Image


def min_max(iterable):
    it = iter(iterable)
    _min = it.next()
    _max = _min
    for element in it:
        if element < _min:
            _min = element
        if element > _max:
            _max = element

    return _min, _max


def is_image_file(_file):
    return os.path.isfile(_file) and _file.endswith('.png')


def list_images(directory):
    files = (os.path.join(directory, _file) for _file in os.listdir(directory))
    image_paths = (_file for _file in files if is_image_file(_file))
    return image_paths


def clear_directory(directory):
    for image in list_images(directory):
        os.remove(image)


def read_pieces(directory):
    image_paths = list_images(directory)
    pieces = [Image.open(f) for f in image_paths]

    sizes = {piece.size for piece in pieces}
    if len(sizes) != 1:
        raise ValueError('not all pieces are compatible by size')

    size = sizes.pop()
    if size[0] != size[1]:
        raise ValueError('pieces are not square')

    return pieces