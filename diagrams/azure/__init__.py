"""
Azure provides a set of services for Microsoft Azure provider.
"""
from __future__ import annotations

from diagrams import Node


class _Azure(Node):
    _provider = "azure"
    _icon_dir = "resources/azure"

    fontcolor = "#ffffff"
