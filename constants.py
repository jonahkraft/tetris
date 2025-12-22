from custom_types import BlockMask, TetrisBlockShape

# WIDTH and HEIGHT must be odd
WIDTH = 13
HEIGHT = 21

BLOCK_SYMBOL = "██"
BLOCK_WIDTH = 2

BLOCK_MASKS: dict[TetrisBlockShape, BlockMask] = {
    TetrisBlockShape.I: (
        False, False, False, False,
        True, True, True, True,
        False, False, False, False,
        False, False, False, False
    ),
    TetrisBlockShape.J: (
        False, False, False, False,
        False, True, False, False,
        False, True, True, True,
        False, False, False, False
    ),
    TetrisBlockShape.L: (
        False, False, False, False,
        False, False, True, False,
        True, True, True, False,
        False, False, False, False
    ),
    TetrisBlockShape.O: (
        False, False, False, False,
        False, True, True, False,
        False, True, True, False,
        False, False, False, False
    ),
    TetrisBlockShape.S: (
        False, False, False, False,
        False, True, True, False,
        True, True, False, False,
        False, False, False, False
    ),
    TetrisBlockShape.T: (
        False, False, False, False,
        False, True, False, False,
        True, True, True, False,
        False, False, False, False
    ),
    TetrisBlockShape.Z: (
        False, False, False, False,
        True, True, False, False,
        False, True, True, False,
        False, False, False, False
    ),
}

BLOCK_COLORS: dict[TetrisBlockShape, int] = {
    TetrisBlockShape.I: 1,
    TetrisBlockShape.J: 2,
    TetrisBlockShape.L: 3,
    TetrisBlockShape.O: 4,
    TetrisBlockShape.S: 5,
    TetrisBlockShape.T: 6,
    TetrisBlockShape.Z: 7
}

COLOR_MAP: dict[str, int] = {
    "cyan": 1,
    "blue": 2,
    "magenta": 3,
    "yellow": 4,
    "green": 5,
    "red": 6,
    "white": 7
}
