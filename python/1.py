'''
1.py
----
Generative art with python
'''

import random
import sys
from typing import Tuple
from collections import namedtuple
from PIL import Image, ImageDraw


DRAWING_SIZE = 2048
OUTPUT_FILENAME = 'pattern_a.jpg'


def make_subsection(coords: Tuple, draw: ImageDraw.Draw, color: Tuple):
    '''
    Draw subsection of the image
    '''
    # Fill
    draw.rectangle(coords, color)


def make_drawing(grid_dims, color_count=3):
    '''
    Draw a grid of images
    '''
    row_len, col_len = grid_dims
    drawing = Image.new('RGB', (DRAWING_SIZE, DRAWING_SIZE))
    draw = ImageDraw.Draw(drawing)
    subsection_width = DRAWING_SIZE / row_len
    subsection_height = DRAWING_SIZE / col_len
    color_pallet = make_color_pallet(color_count)

    for x in range(row_len):
        for y in range(col_len):
            subsection_top_left_x = x * subsection_width
            subsection_top_left_y = y * subsection_height
            subsection_bottom_right_x = subsection_top_left_x + subsection_width
            subsection_bottom_right_y = subsection_top_left_y + subsection_height
            fill_color_idx = (x + y) % len(color_pallet)
            fill_color = color_pallet[fill_color_idx]
            make_subsection(
                (
                    subsection_top_left_x,
                    subsection_top_left_y,
                    subsection_bottom_right_x,
                    subsection_bottom_right_y,
                ),
                draw,
                fill_color
            )

    drawing.save(OUTPUT_FILENAME)


def make_color_pallet(color_count: int):
    '''
    Generate an appropriate color pallet out of
    complementary colors
    '''
    random_gen = lambda: random.randint(0, 255)
    random_colors = [(random_gen(), random_gen(), random_gen()) for count in range(color_count)]
    complementary_colors = [get_complementary_color(c) for c in random_colors]
    return [c for row in zip(random_colors, complementary_colors) for c in row]


def get_complementary_color(color: Tuple) -> Tuple:
    return tuple(255 - c for c in color)


if __name__ == "__main__":
    grid_dims = 4
    make_drawing((grid_dims, grid_dims))
