# [Ansible role nvim](#ansible-role-nvim)

Install and Configure NVIM on your Linux systems.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/buluma/ansible-role-nvim/workflows/Ansible%20Molecule/badge.svg)](https://github.com/buluma/ansible-role-nvim/actions)|[![gitlab](https://gitlab.com/shadowwalker/ansible-role-nvim/badges/master/pipeline.svg)](https://gitlab.com/shadowwalker/ansible-role-nvim)|[![downloads](https://img.shields.io/ansible/role/d/buluma/nvim)](https://galaxy.ansible.com/buluma/nvim)|[![Version](https://img.shields.io/github/release/buluma/ansible-role-nvim.svg)](https://github.com/buluma/ansible-role-nvim/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/buluma/ansible-role-nvim/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true
  vars:
    nvim_user: shadowwalker
    neovim: true
    neovim_nightly: false
    neovim_pip3_state: false
    treesitter: true
  tasks:
    - name: Adding user
      ansible.builtin.user:
        name: "{{ nvim_user }}"
        create_home: true
        shell: /bin/bash

    - name: Run nvim role
      ansible.builtin.include_role:
        name: ansible-role-nvim
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/buluma/ansible-role-nvim/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: buluma.bootstrap
    - role: buluma.ca_certificates
```

Also see a [full explanation and example](https://buluma.github.io/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/buluma/ansible-role-nvim/blob/master/defaults/main.yml):

```yaml
# Default variables for 'neovim' role
#
# These variables have the lowest priority of any variables available, and can
# be easily overridden by any other variable, including inventory variables.
#
# (See Using Variables for more information)
# https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#playbooks-variables
---
# application versions
neovim_version: "0.9.5"
treesitter_version: "0.22.2"

# variables for downloading appimages
nvim_dl_dir: "/opt/nvim/{{ neovim_version }}"
nvim_appimage_url: "https://github.com/neovim/neovim/releases/download/v{{ neovim_version }}/nvim.appimage"
treesitter_dl_dir: "/opt/treesitter/{{ treesitter_version }}"
treesitter_dl_name: "tree-sitter-linux-x64.gz"
treesitter_archive_url: "https://github.com/tree-sitter/tree-sitter/releases/download/v{{ treesitter_version }}/{{ treesitter_dl_name }}"
treesitter_filename: "tree-sitter-linux-x64"

# toggles for end-users
neovim: true
treesitter: true
neovim_nightly: false

neovim_pde: false
neovim_apt_packages: []
neovim_pip_packages: []
neovim_npm_packages: []
neovim_config_dirs: []
neovim_external_config: []
neovim_config_syncs: []

# digging deeper
neovim_pip3_packager_state: latest
neovim_npm_packager_state: latest
neovim_pip3_state: latest
neovim_apt_state: latest
...
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/buluma/ansible-role-nvim/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[buluma.bootstrap](https://galaxy.ansible.com/buluma/bootstrap)|[![Build Status GitHub](https://github.com/buluma/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/buluma/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/shadowwalker/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/shadowwalker/ansible-role-bootstrap)|
|[buluma.ca_certificates](https://galaxy.ansible.com/buluma/ca_certificates)|[![Build Status GitHub](https://github.com/buluma/ansible-role-ca_certificates/workflows/Ansible%20Molecule/badge.svg)](https://github.com/buluma/ansible-role-ca_certificates/actions)|[![Build Status GitLab](https://gitlab.com/shadowwalker/ansible-role-ca_certificates/badges/master/pipeline.svg)](https://gitlab.com/shadowwalker/ansible-role-ca_certificates)|

## [Context](#context)

This role is part of many compatible roles. Have a look at [the documentation of these roles](https://buluma.github.io/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/buluma/ansible-role-nvim/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/buluma):

|container|tags|
|---------|----|
|[Fedora](https://hub.docker.com/r/buluma/fedora)|all|
|[Ubuntu](https://hub.docker.com/r/buluma/ubuntu)|all|
|[Debian](https://hub.docker.com/r/buluma/debian)|all|

The minimum version of Ansible required is 2.4, tests have been done on:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them on [GitHub](https://github.com/buluma/ansible-role-nvim/issues).

## [License](#license)

[Apache-2.0](https://github.com/buluma/ansible-role-nvim/blob/master/LICENSE).

## [Author Information](#author-information)

[buluma](https://buluma.github.io/)

