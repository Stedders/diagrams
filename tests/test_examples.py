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


def test_event_processing_on_aws():
    from diagrams import Cluster, Diagram
    from diagrams.aws.compute import ECS, EKS, Lambda
    from diagrams.aws.database import Redshift
    from diagrams.aws.integration import SQS
    from diagrams.aws.storage import S3

    with Diagram(
        "Event Processing",
        directory=Path(__file__).parent / "test_output",
        show=False,
    ):
        source = EKS("k8s source")

        with Cluster("Event Flows"):
            with Cluster("Event Workers"):
                workers = [
                    ECS("worker1"),
                    ECS("worker2"),
                    ECS("worker3"),
                ]

            queue = SQS("event queue")

            with Cluster("Processing"):
                handlers = [
                    Lambda("proc1"),
                    Lambda("proc2"),
                    Lambda("proc3"),
                ]

        store = S3("events store")
        dw = Redshift("analytics")

        source >> workers >> queue >> handlers
        handlers >> store
        handlers >> dw

    assert filecmp.cmp(
        Path(__file__).parent / "test_output/event_processing.png",
        Path(__file__).parent / "test_results/event_processing.png",
    )


def test_message_collecting_system_on_gcp():
    from diagrams import Cluster, Diagram
    from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub
    from diagrams.gcp.compute import AppEngine, Functions
    from diagrams.gcp.database import BigTable
    from diagrams.gcp.iot import IotCore
    from diagrams.gcp.storage import GCS

    with Diagram(
        "Message Collecting",
        show=False,
        directory=Path(__file__).parent / "test_output",
    ):
        pubsub = PubSub("pubsub")

        with Cluster("Source of Data"):
            [
                IotCore("core1"),
                IotCore("core2"),
                IotCore("core3"),
            ] >> pubsub

        with Cluster("Targets"):
            with Cluster("Data Flow"):
                flow = Dataflow("data flow")

            with Cluster("Data Lake"):
                flow >> [
                    BigQuery("bq"),
                    GCS("storage"),
                ]

            with Cluster("Event Driven"):
                with Cluster("Processing"):
                    flow >> AppEngine("engine") >> BigTable("bigtable")

                with Cluster("Serverless"):
                    flow >> Functions("func") >> AppEngine("appengine")

        pubsub >> flow

    assert filecmp.cmp(
        Path(__file__).parent / "test_output/message_collecting.png",
        Path(__file__).parent / "test_results/message_collecting.png",
    )


def test_exposed_pod_with_3_replicas():
    from diagrams import Diagram
    from diagrams.k8s.clusterconfig import HPA
    from diagrams.k8s.compute import Deployment, Pod, ReplicaSet
    from diagrams.k8s.network import Ingress, Service

    with Diagram(
        "Exposed Pod with 3 Replicas",
        show=False,
        directory=Path(__file__).parent / "test_output",
    ):
        net = Ingress("domain.com") >> Service("svc")
        (
            net
            >> [
                Pod("pod1"),
                Pod("pod2"),
                Pod("pod3"),
            ]
            << ReplicaSet("rs")
            << Deployment("dp")
            << HPA("hpa")
        )

    assert filecmp.cmp(
        Path(__file__).parent / "test_output/exposed_pod_with_3_replicas.png",
        Path(__file__).parent / "test_results/exposed_pod_with_3_replicas.png",
    )


def test_advanced_web_service_with_on_premise():
    from diagrams import Cluster, Diagram
    from diagrams.onprem.analytics import Spark
    from diagrams.onprem.compute import Server
    from diagrams.onprem.database import PostgreSQL
    from diagrams.onprem.inmemory import Redis
    from diagrams.onprem.aggregator import Fluentd
    from diagrams.onprem.monitoring import Grafana, Prometheus
    from diagrams.onprem.network import Nginx
    from diagrams.onprem.queue import Kafka

    with Diagram(
        "Advanced Web Service with On-Premise",
        show=False,
        directory=Path(__file__).parent / "test_output",
    ):
        ingress = Nginx("ingress")

        metrics = Prometheus("metric")
        metrics << Grafana("monitoring")

        with Cluster("Service Cluster"):
            grpcsvc = [
                Server("grpc1"),
                Server("grpc2"),
                Server("grpc3"),
            ]

        with Cluster("Sessions HA"):
            primary = Redis("session")
            primary - Redis("replica") << metrics
            grpcsvc >> primary

        with Cluster("Database HA"):
            primary = PostgreSQL("users")
            primary - PostgreSQL("replica") << metrics
            grpcsvc >> primary

        aggregator = Fluentd("logging")
        aggregator >> Kafka("stream") >> Spark("analytics")

        ingress >> grpcsvc >> aggregator

    assert filecmp.cmp(
        Path(__file__).parent / "test_output/advanced_web_service_with_on-premise.png",
        Path(__file__).parent / "test_results/advanced_web_service_with_on-premise.png",
    )
