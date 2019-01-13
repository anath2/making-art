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


LIST_SYM = []


DrawingCoords = namedtuple(
    'DrawingCoords',
    [
        'top_left_x',
        'top_left_y',
        'bottom_right_x',
        'bottom_right_y'
    ]
)


def draw_block(boundary: DrawingCoords, block_size: int,  draw: ImageDraw.Draw, element: int, random_color: Tuple):
    '''
    Draw block
    '''
    if (element == int(block_size / 2)):
        draw.rectangle(
            (
                boundary.top_left_x,
                boundary.top_left_y,
                boundary.bottom_right_x,
                boundary.bottom_right_y
            ),
            random_color
        )
    elif len(LIST_SYM) == element + 1:
        draw.rectangle(
            (
                boundary.top_left_x,
                boundary.top_left_y,
                boundary.bottom_right_x,
                boundary.bottom_right_y
            ),
            random_color
        )
    else:
        LIST_SYM.append(random_color)
        draw.rectangle(
            (
                boundary.top_left_x,
                boundary.top_left_y,
                boundary.bottom_right_x,
                boundary.bottom_right_y
            ),
            random_color
        )

def make_drawing(boundary: DrawingCoords, draw: ImageDraw.Draw, drawing_size: int):
    '''
    Draw a single images
    '''
    frame_top_left_x = boundary.top_left_x
    frame_top_left_y = boundary.top_left_y
    frame_bottom_right_x = boundary.bottom_right_x
    frame_bottom_right_y = boundary.bottom_right_y

    block_size = (frame_bottom_right_x - frame_top_left_x) / drawing_size
    random_gen = lambda: random.randint(50,215) # rang for color
    random_color = lambda: (random_gen(), random_gen(), random_gen())

    random_color_list = [
        random_color(),
        random_color(),
        random_color(),
        (0,0,0),
        (0,0,0),
        (0,0,0)
    ]
    i = 0

    for y in range(drawing_size):
        i *= -1
        element = 0
        for x in range(drawing_size):
            top_left_x = x * block_size + frame_top_left_x
            top_left_y = y * block_size + frame_top_left_y
            bottom_right_x = top_left_x + block_size
            bottom_right_y = top_left_y + block_size
            boundary = DrawingCoords(
                top_left_x=top_left_x,
                top_left_y=top_left_y,
                bottom_right_x=bottom_right_x,
                bottom_right_y=bottom_right_y
            )
            draw_block(
                boundary,
                block_size,
                draw,
                element,
                random.choice(random_color_list)
            )
            if element == int(drawing_size / 2) or element == 0:
                i *= -1
            element += i


def generate_img(drawing_count: int, drawing_size: int, image_size: int):
    '''
    Draw a grid of images
    ARGS:
        figure_size: The size of figure inside the grid
        figure_count: The number of images
        image_size: Total size of the image or canvas
    '''
    image = Image.new('RGB', (image_size, image_size))
    draw = ImageDraw.Draw(image)
    frame_size = image_size / drawing_count
    padding = frame_size / drawing_size
    output_filename = '1.jpeg'

    for x in range(0, drawing_count):
        for y in range(0, drawing_count):
            top_left_x = x*frame_size + padding / 2
            top_left_y = y * frame_size + padding / 2
            bottom_right_x = top_left_x + frame_size - padding
            bottom_right_y = top_left_y + frame_size - padding

    boundary = DrawingCoords(
        top_left_x=top_left_x,
        top_left_y=top_left_y,
        bottom_right_x=bottom_right_x,
        bottom_right_y=bottom_right_y
    )
    make_drawing(boundary, draw, drawing_size)
    image.save(output_filename)


if __name__ == "__main__":
    drawing_count = int(sys.argv[1])
    drawing_size = int(sys.argv[2])
    image_size = int(sys.argv[3])
    generate_img(drawing_count, drawing_size, image_size)
