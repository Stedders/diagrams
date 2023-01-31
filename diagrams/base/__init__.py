"""
Base provides a set of general services for backend infrastructure.
"""
from __future__ import annotations

from diagrams import Node


class _Base(Node):
    _provider = "base"
    _icon_dir = "resources/base"

    fontcolor = "#ffffff"
