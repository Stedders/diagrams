from __future__ import annotations

from pathlib import Path

import pytest


@pytest.fixture(scope="session", autouse=True)
def clean_output():
    for png in (Path(__file__).parent / "test_output").glob("*.png"):
        png.unlink()
