import tga


def test_package():
    assert tga.__version__ is not None
    assert tga.Image is not None
    assert tga.Color is not None
