from enum import auto
from strenum import StrEnum, LowercaseStrEnum


class Directions(StrEnum):
    TB = auto()
    BT = auto()
    LR = auto()
    RL = auto()


class CurveStyles(LowercaseStrEnum):
    Ortho = auto()
    Curved = auto()


class OutputFormats(LowercaseStrEnum):
    PNG = auto()
    JPG = auto()
    SVG = auto()
    PDF = auto()
    DOT = auto()
