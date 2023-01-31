# This module is automatically generated by autogen.sh. DO NOT EDIT.
from __future__ import annotations

from . import _OnPrem


class _Vcs(_OnPrem):
    _type = "vcs"
    _icon_dir = "resources/onprem/vcs"


class Git(_Vcs):
    _icon = "git.png"


class Gitea(_Vcs):
    _icon = "gitea.png"


class Github(_Vcs):
    _icon = "github.png"


class Gitlab(_Vcs):
    _icon = "gitlab.png"


class Svn(_Vcs):
    _icon = "svn.png"


# Aliases
