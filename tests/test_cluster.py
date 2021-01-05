from pathlib import Path

from pytest_kind import KindCluster


def test_cluster_name():
    cluster = KindCluster("foo")
    assert cluster.name == "foo"


def test_cluster_kubeconfig():
    path = Path("/tmp/test.yaml")
    cluster = KindCluster("foo", path)
    assert cluster.kubeconfig_path == path


def test_create_delete():
    cluster = KindCluster("pytest-kind-test-create-delete")
    try:
        cluster.create()
    finally:
        cluster.delete()
