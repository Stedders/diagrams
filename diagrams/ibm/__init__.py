"""
IBM provides a set of services for IBM Cloud provider.
"""
from __future__ import annotations

from diagrams import Node


class _IBM(Node):
    _provider = "ibm"
    _icon_dir = "resources/ibm"

    fontcolor = "#ffffff"
