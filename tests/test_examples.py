from __future__ import annotations

import filecmp
from pathlib import Path


def test_groupd_works_aws():
    from diagrams import Diagram
    from diagrams.aws.compute import EC2
    from diagrams.aws.database import RDS
    from diagrams.aws.network import ELB

    with Diagram(
        "Grouped Workers",
        directory=Path(__file__).parent / "test_output",
        show=False,
        direction="TB",
        outformat="png",
    ):
        (
            ELB("lb")
            >> [
                EC2("worker1"),
                EC2("worker2"),
                EC2("worker3"),
                EC2("worker4"),
                EC2("worker5"),
            ]
            >> RDS("events")
        )

    assert filecmp.cmp(
        Path(__file__).parent / "test_output/grouped_workers.png",
        Path(__file__).parent / "test_results/grouped_workers.png",
    )


def test_clustered_web_services():
    from diagrams import Cluster, Diagram
    from diagrams.aws.compute import ECS
    from diagrams.aws.database import ElastiCache, RDS
    from diagrams.aws.network import ELB
    from diagrams.aws.network import Route53

    with Diagram(
        "Clustered Web Services",
        show=False,
        directory=Path(__file__).parent / "test_output",
        direction="TB",
        outformat="png",
    ):
        dns = Route53("dns")
        lb = ELB("lb")

        with Cluster("Services"):
            svc_group = [
                ECS("web1"),
                ECS("web2"),
                ECS("web3"),
            ]

        with Cluster("DB Cluster"):
            db_primary = RDS("userdb")
            db_primary - [RDS("userdb ro")]

        memcached = ElastiCache("memcached")

        dns >> lb >> svc_group
        svc_group >> db_primary
        svc_group >> memcached

    assert filecmp.cmp(
        Path(__file__).parent / "test_output/clustered_web_services.png",
        Path(__file__).parent / "test_results/clustered_web_services.png",
    )
