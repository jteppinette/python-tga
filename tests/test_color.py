import pytest

from tga.color import Color


def test_init_rgb():
    white = Color(255, 255, 255)

    assert white.red == 255
    assert white.green == 255
    assert white.blue == 255


def test_init_rgba():
    transparent = Color(255, 255, 255, 0)

    assert transparent.red == 255
    assert transparent.green == 255
    assert transparent.blue == 255
    assert transparent.alpha == 0


def test_from_int_rgb():
    white = Color.from_int(255, 255, 255)

    assert white.red == 255
    assert white.green == 255
    assert white.blue == 255


def test_from_int_rgba():
    transparent = Color.from_int(255, 255, 255, 0)

    assert transparent.red == 255
    assert transparent.green == 255
    assert transparent.blue == 255
    assert transparent.alpha == 0


@pytest.mark.parametrize(
    "color, other, expected",
    [
        (Color.from_int(255, 255, 255), Color.from_int(255, 255, 255), True),
        (Color.from_int(255, 255, 255), Color.from_int(0, 255, 255), False),
        (Color.from_int(255, 255, 255), Color.from_int(255, 255, 255, 255), False),
        (Color.from_int(255, 255, 255), Color.from_int(255, 255, 255, 0), False),
    ],
)
def test_equality(color, other, expected):
    is_equal = color == other
    assert is_equal is expected
