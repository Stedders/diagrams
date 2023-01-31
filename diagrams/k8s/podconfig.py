# This module is automatically generated by autogen.sh. DO NOT EDIT.
from __future__ import annotations

from . import _K8S


class _Podconfig(_K8S):
    _type = "podconfig"
    _icon_dir = "resources/k8s/podconfig"


class CM(_Podconfig):
    _icon = "cm.png"


class Secret(_Podconfig):
    _icon = "secret.png"


# Aliases

ConfigMap = CM
