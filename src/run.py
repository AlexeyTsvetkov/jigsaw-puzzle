#!/usr/bin/python
# -*-coding: utf-8 -*-

import os
import argparse

from PIL import Image

import measures
from puzzle_generator import generate_puzzle
from puzzle_solver import PuzzleSolver
from helpers import read_pieces


def parse_args():
    parser = argparse.ArgumentParser()

    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('-g', '--generate',  action='store_true')
    mode.add_argument('-s', '--solve',  action='store_true')
    parser.add_argument('-i', '--input', required=True, help='path to original image or puzzle directory')
    parser.add_argument('-o', '--output', required=True,
                        help='where to save generated puzzle or solved puzzle image')
    parser.add_argument('-ps', '--piece_size', type=int, default=0, help='desired piece size')
    parser.add_argument('-pw', '--puzzle_width', type=int, default=0, help='puzzle width (in pieces)')
    parser.add_argument('-ph', '--puzzle_height', type=int, default=0, help='puzzle height (in pieces)')

    args = parser.parse_args()
    if args.generate:
        if not args.piece_size:
            parser.error('-ps/--piece_size is required when generating puzzle')
        if args.piece_size <= 0:
            parser.error('-ps/--piece_size should be positive integer')
        if not os.path.isfile(args.input):
            parser.error('-i/--input should be an existing image file for puzzle generation')
        if os.path.isfile(args.output):
            parser.error('-o/--output should be directory for puzzle generation (created if not exists)')
    else:
        if not args.puzzle_width or not args.puzzle_height:
            parser.error('-pw/--puzzle_width and -ph/--puzzle_height are required for puzzle solving')
        if args.puzzle_width < 0 or args.puzzle_height < 0:
            parser.error('-pw/--puzzle_width and -ph/--puzzle_height should be positive integers')
        if not os.path.isdir(args.input):
            parser.error('-i/--input should be an existing directory for puzzle solving')

    return args

if __name__ == '__main__':
    args = parse_args()
    if args.generate:
        if not os.path.exists(args.output):
            os.makedirs(args.output)

        image = Image.open(args.input)
        pieces, puzzle_width, puzzle_height = generate_puzzle(image, args.piece_size)
        for i, piece in enumerate(pieces):
            piece_path = os.path.join(args.output, '%i.png' % (i,))
            piece.save(piece_path)

        print 'Puzzle saved to: %s' % (args.output,)
        print 'Puzzle sizes: width=%i, height=%i' % (puzzle_width, puzzle_height)
    else:
        solver = PuzzleSolver(measures.rgb_mgc)

        pieces = read_pieces(args.input)
        solution = solver.solve_puzzle(pieces, args.puzzle_height, args.puzzle_width)
        solution.save(args.output)

        print 'Resulting image saved to: %s' % (args.output,)