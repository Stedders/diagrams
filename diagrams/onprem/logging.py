# This module is automatically generated by autogen.sh. DO NOT EDIT.
from __future__ import annotations

from . import _OnPrem


class _Logging(_OnPrem):
    _type = "logging"
    _icon_dir = "resources/onprem/logging"


class Fluentbit(_Logging):
    _icon = "fluentbit.png"


class Graylog(_Logging):
    _icon = "graylog.png"


class Loki(_Logging):
    _icon = "loki.png"


class Rsyslog(_Logging):
    _icon = "rsyslog.png"


class SyslogNg(_Logging):
    _icon = "syslog-ng.png"


# Aliases

FluentBit = Fluentbit
RSyslog = Rsyslog
