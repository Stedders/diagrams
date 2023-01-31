"""
OCI provides a set of services for Oracle Cloud Infrastructure provider.
"""
from __future__ import annotations

from diagrams import Node


class _OCI(Node):
    _provider = "oci"
    _icon_dir = "resources/oci"

    fontcolor = "#312D2A"
