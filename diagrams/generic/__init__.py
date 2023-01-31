"""
Generic provides the possibility of load an image to be presented as a node.
"""
from __future__ import annotations

from diagrams import Node


class _Generic(Node):
    provider = "generic"
    _icon_dir = "resources/generic"

    fontcolor = "#ffffff"
