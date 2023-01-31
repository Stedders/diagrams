# This module is automatically generated by autogen.sh. DO NOT EDIT.
from __future__ import annotations

from . import _OpenStack


class _Baremetal(_OpenStack):
    _type = "baremetal"
    _icon_dir = "resources/openstack/baremetal"


class Cyborg(_Baremetal):
    _icon = "cyborg.png"


class Ironic(_Baremetal):
    _icon = "ironic.png"


# Aliases
