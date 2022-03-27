import struct

import pytest

from tga.color import Color
from tga.image import Image, ImageDepth, ImageType


@pytest.mark.parametrize(
    "width, height, color", [(10, 10, None), (10, 10, Color.from_int(0, 0, 0, 0))]
)
def test_init(width, height, color):

    if color is None:
        image = Image(width, height)
    else:
        image = Image(width, height, color)

    assert image.width == width
    assert image.height == width

    defualt_color = Color.from_int(255, 255, 255)

    for row in range(width):
        for column in range(height):
            cell = image.data[row][column]

            if color is None:
                assert cell == defualt_color
            else:
                assert cell == color


def test_empty_to_bytes():
    image = Image(0, 0)
    data = image.to_bytes()

    assert data is not None
    assert len(data) == 18

    (
        id_length,
        color_map_type,
        image_type,
        color_map_origin,
        color_map_length,
        color_map_depth,
        x_origin,
        y_origin,
        width,
        height,
        depth,
        descriptor,
    ) = struct.unpack("<BBBHHBHHHHBB", data)

    assert id_length == 0
    assert color_map_type == 0
    assert image_type == ImageType.UNCOMPRESSED_RGB

    # color map specification
    assert color_map_origin == 0
    assert color_map_length == 0
    assert color_map_depth == 0

    # image specification
    assert x_origin == 0
    assert y_origin == 0
    assert width == 0
    assert height == 0
    assert depth == ImageDepth.TARGA_24
    assert descriptor == 0


def test_non_empty_to_bytes():
    WIDTH = 2
    HEIGHT = 2

    image = Image(WIDTH, HEIGHT)
    data = image.to_bytes()

    assert data is not None
    assert len(data) == 18 + (WIDTH * HEIGHT * ImageDepth.TARGA_24 // 8) == 30

    (
        id_length,
        color_map_type,
        image_type,
        color_map_origin,
        color_map_length,
        color_map_depth,
        x_origin,
        y_origin,
        width,
        height,
        depth,
        descriptor,
    ) = struct.unpack("<BBBHHBHHHHBB", data[:18])

    assert id_length == 0
    assert color_map_type == 0
    assert image_type == ImageType.UNCOMPRESSED_RGB

    # color map specification
    assert color_map_origin == 0
    assert color_map_length == 0
    assert color_map_depth == 0

    # image specification
    assert x_origin == 0
    assert y_origin == 0
    assert width == WIDTH
    assert height == HEIGHT
    assert depth == ImageDepth.TARGA_24
    assert descriptor == 0

    # image data
    assert len(data[18:]) == WIDTH * HEIGHT * ImageDepth.TARGA_24 // 8 == 12

    for value in data[18:]:
        assert value == 255
