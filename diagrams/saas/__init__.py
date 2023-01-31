"""
Saas provides a set of general saas services.
"""
from __future__ import annotations

from diagrams import Node


class _Saas(Node):
    _provider = "saas"
    _icon_dir = "resources/saas"

    fontcolor = "#ffffff"
