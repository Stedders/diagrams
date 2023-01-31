from __future__ import annotations

import filecmp
from pathlib import Path


def test_mega_check():
    from diagrams import Diagram, Cluster
    from diagrams.alibabacloud.analytics import AnalyticDb
    from diagrams.alibabacloud.application import ApiGateway
    from diagrams.alibabacloud.communication import DirectMail
    from diagrams.alibabacloud.compute import AutoScaling
    from diagrams.alibabacloud.database import ApsaradbHbase
    from diagrams.alibabacloud.iot import IotPlatform
    from diagrams.alibabacloud.network import ServerLoadBalancer
    from diagrams.alibabacloud.security import SecurityCenter
    from diagrams.alibabacloud.storage import CloudStorageGateway
    from diagrams.alibabacloud.web import Domain

    with Diagram(
        "mega check",
        show=False,
        directory=Path(__file__).parent / "test_output",
    ):
        with Cluster("alibaba"):
            (
                AnalyticDb("analytic db")
                >> ApiGateway("gateway")
                >> DirectMail("mail")
                >> AutoScaling(
                    "scaling",
                )
                >> ApsaradbHbase("DB")
                >> IotPlatform("iot")
                >> ServerLoadBalancer("load")
                >> SecurityCenter(
                    "security",
                )
                >> CloudStorageGateway("cloud storage")
                >> Domain("domain")
            )

    assert filecmp.cmp(
        Path(__file__).parent / "test_output/mega_check.png",
        Path(__file__).parent / "test_results/mega_check.png",
    )
