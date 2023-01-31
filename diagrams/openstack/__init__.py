"""
Openstack provides a set of general OpenStack services.
"""
from __future__ import annotations

from diagrams import Node


class _OpenStack(Node):
    _provider = "openstack"
    _icon_dir = "resources/openstack"

    fontcolor = "#ffffff"
