"""
Elastic provides a set of general elastic services.
"""
from __future__ import annotations

from diagrams import Node


class _Elastic(Node):
    _provider = "elastic"
    _icon_dir = "resources/elastic"

    fontcolor = "#ffffff"
