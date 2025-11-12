# Ansible role consul-service

Ansible role defining a Consul service. It'll
- Install Consul via `brianshumate.consul` as an agent.
- Define a service with a file in `/etc/consul/consul.d/<consul_service_name>.yml`

This role is tested using [Molecule](https://molecule.readthedocs.io/). The
default will use Docker that you must install yourself. Then run `tox` to setup
python environment and start testing.

## Requirements

Python & [tox](https://tox.readthedocs.io). See imports in `library/*` and tasks in `molecule/default/converge.yml` if any specific, but those should be added in `tox.ini`.

## Role Variables

See [defaults/main.yml](defaults/main.yml).

## Dependencies

See [meta/main.yml](meta/main.yml) and [molecule/default/requirements.yml](molecule/default/requirements.yml) if any.

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
