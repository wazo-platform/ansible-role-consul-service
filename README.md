# Ansible role consul-service

Ansible role defining a Consul service. It'll
- Install Consul via `wazo.consul` as an agent.
- Define a service with a file in `/etc/consul.d/<consul_service_name>.service.json`

This role is tested using [Molecule](https://molecule.readthedocs.io/). The
default will use Docker that you must install yourself. Then run `tox` to setup
python environment and start testing.

## Requirements

Python & [tox](https://tox.readthedocs.io). See imports in `library/*` and tasks in `molecule/default/converge.yml` if any specific, but those should be added in `tox.ini`.

## Role Variables

See [defaults/main.yml](defaults/main.yml).

## Dependencies

This role requires the following roles to be installed on the controller:

- `wazo.metadata` — declared in [meta/main.yml](meta/main.yml), so it is always
  run as a dependency of this role.
- `wazo.consul` — **not** a meta dependency. It is included conditionally at
  runtime (only when Consul is not already installed) via `include_role` in
  [tasks/main.yml](tasks/main.yml). Because `include_role` does not install the
  role, `wazo.consul` must already be present on the roles path for this role to
  work.

Install both with:

```sh
ansible-galaxy install -r requirements.yml
```

See also [meta/main.yml](meta/main.yml) and
[molecule/default/requirements.yml](molecule/default/requirements.yml).

## Example Playbook

```yaml
- hosts: all
  roles:
    - wazo.consul-service
```

## License

MIT

## Author Information

Wazo Developers for Wazo https://wazo.io
