# This module is automatically generated by autogen.sh. DO NOT EDIT.
from __future__ import annotations

from . import _OCI


class _Compute(_OCI):
    _type = "compute"
    _icon_dir = "resources/oci/compute"


class AutoscaleWhite(_Compute):
    _icon = "autoscale-white.png"


class Autoscale(_Compute):
    _icon = "autoscale.png"


class BMWhite(_Compute):
    _icon = "bm-white.png"


class BM(_Compute):
    _icon = "bm.png"


class ContainerWhite(_Compute):
    _icon = "container-white.png"


class Container(_Compute):
    _icon = "container.png"


class FunctionsWhite(_Compute):
    _icon = "functions-white.png"


class Functions(_Compute):
    _icon = "functions.png"


class InstancePoolsWhite(_Compute):
    _icon = "instance-pools-white.png"


class InstancePools(_Compute):
    _icon = "instance-pools.png"


class OCIRWhite(_Compute):
    _icon = "ocir-white.png"


class OCIR(_Compute):
    _icon = "ocir.png"


class OKEWhite(_Compute):
    _icon = "oke-white.png"


class OKE(_Compute):
    _icon = "oke.png"


class VMWhite(_Compute):
    _icon = "vm-white.png"


class VM(_Compute):
    _icon = "vm.png"


# Aliases

VirtualMachine = VM
VirtualMachineWhite = VMWhite
BareMetal = BM
BareMetalWhite = BMWhite
OCIRegistry = OCIR
OCIRegistryWhite = OCIRWhite
ContainerEngine = OKE
ContainerEngineWhite = OKEWhite
