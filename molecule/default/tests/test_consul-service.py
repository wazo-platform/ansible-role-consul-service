import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "name",
    ["procps"],
)
def test_packages(host, name):
    item = host.package(name)
    assert item.is_installed


def test_user(host):
    u = host.user("consul")
    assert u.exists


@pytest.mark.parametrize(
    "path",
    [
        "/etc/consul/.consul_bootstrapped",
        "/etc/consul/consul.d/default-service.service.json",
    ],
)
def test_files(host, path):
    with host.sudo():
        item = host.file(path)
        assert item.exists


@pytest.mark.parametrize("name", ["consul"])
def test_services(host, name):
    item = host.service(name)
    assert item.is_running
    assert item.is_enabled


def test_service_file_content(host):
    with host.sudo():
        service = host.file(
            "/etc/consul/consul.d/default-service.service.json"
        ).content_string
        assert "testtag" in service
        assert "published" in service
        assert '"URL"' in service
        assert '"URL2"' not in service
        assert '"URL3"' not in service
        assert '"URL4"' in service
        assert '"URL5"' not in service
