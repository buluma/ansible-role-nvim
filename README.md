# Ansible role [nvim](https://galaxy.ansible.com/ui/standalone/roles/buluma/nvim/documentation)

Ansible role to install nvim configuration

|GitHub|Version|Issues|Pull Requests|Downloads|
|------|-------|------|-------------|---------|
|[![github](https://github.com/buluma/ansible-role-nvim/actions/workflows/molecule.yml/badge.svg)](https://github.com/buluma/ansible-role-nvim/actions/workflows/molecule.yml)|[![Version](https://img.shields.io/github/release/buluma/ansible-role-nvim.svg)](https://github.com/buluma/ansible-role-nvim/releases/)|[![Issues](https://img.shields.io/github/issues/buluma/ansible-role-nvim.svg)](https://github.com/buluma/ansible-role-nvim/issues/)|[![PullRequests](https://img.shields.io/github/issues-pr-closed-raw/buluma/ansible-role-nvim.svg)](https://github.com/buluma/ansible-role-nvim/pulls/)|[![Ansible Role](https://img.shields.io/ansible/role/d/buluma/nvim)](https://galaxy.ansible.com/ui/standalone/roles/buluma/nvim/documentation)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/buluma/ansible-role-nvim/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  vars:
    nvim_user: hurricanehrndz
    fnm_install_npmrc: true
    fnm_npmrc_suffix: ".config/npm/config"
  tasks:
    - name: Add hurricanehrndz user
      user:
        name: "{{ nvim_user }}"
        create_home: yes
        shell: /bin/bash

    - name: Run nvim role
      include_role:
        name: nvim
```

Also see a [full explanation and example](https://buluma.github.io/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/buluma/ansible-role-nvim/blob/master/defaults/main.yml):

```yaml
---
# defaults file for ansible-nvim
nvim_user: "{{ ansible_user | default(lookup('env', 'USER')) }}"

nvim_python_ver: 3.9.0

nvim_python_mods:
  - pynvim
  - neovim-remote
  - pyls-mypy
  - "python-language-server[all]"

nvim_git_repo: https://github.com/hurricanehrndz/nvim.git
nvim_git_branch: lua
nvim_fzf_bin_only: false
nvim_fnm_root_suffix: ".local/share/fnm"
nvim_pyenv_root_suffix: ".local/share/pyenv"
nvim_nodejs_version: "14.15.0"
nvim_npm_global_pkgs:
  - name: neovim

# install fzf
nvim_install_fzf: true

# allow crates override
nvim_cargo_crates: []
nvim_install_rls: true

# lsp servers to install
nvim_lsp_servers:
  - yamlls
  - bashls
  - tsserver
  - vimls
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/buluma/ansible-role-nvim/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | Version |
|-------------|--------|--------|
|[buluma.bootstrap](https://galaxy.ansible.com/buluma/bootstrap)|[![Ansible Molecule](https://github.com/buluma/ansible-role-bootstrap/actions/workflows/molecule.yml/badge.svg)](https://github.com/buluma/ansible-role-bootstrap/actions/workflows/molecule.yml)|[![Version](https://img.shields.io/github/release/buluma/ansible-role-bootstrap.svg)](https://github.com/shadowwalker/ansible-role-bootstrap)|
|[hurricanehrndz.pyenv](https://galaxy.ansible.com/buluma/hurricanehrndz.pyenv)|[![Ansible Molecule](https://github.com/buluma/hurricanehrndz.pyenv/actions/workflows/molecule.yml/badge.svg)](https://github.com/buluma/hurricanehrndz.pyenv/actions/workflows/molecule.yml)|[![Version](https://img.shields.io/github/release/buluma/hurricanehrndz.pyenv.svg)](https://github.com/shadowwalker/hurricanehrndz.pyenv)|
|[hurricanehrndz.fnm](https://galaxy.ansible.com/buluma/hurricanehrndz.fnm)|[![Ansible Molecule](https://github.com/buluma/hurricanehrndz.fnm/actions/workflows/molecule.yml/badge.svg)](https://github.com/buluma/hurricanehrndz.fnm/actions/workflows/molecule.yml)|[![Version](https://img.shields.io/github/release/buluma/hurricanehrndz.fnm.svg)](https://github.com/shadowwalker/hurricanehrndz.fnm)|
|[hurricanehrndz.rustup](https://galaxy.ansible.com/buluma/hurricanehrndz.rustup)|[![Ansible Molecule](https://github.com/buluma/hurricanehrndz.rustup/actions/workflows/molecule.yml/badge.svg)](https://github.com/buluma/hurricanehrndz.rustup/actions/workflows/molecule.yml)|[![Version](https://img.shields.io/github/release/buluma/hurricanehrndz.rustup.svg)](https://github.com/shadowwalker/hurricanehrndz.rustup)|

## [Dependencies](#dependencies)

Most roles require some kind of preparation, this is done in `molecule/default/prepare.yml`. This role has a "hard" dependency on the following roles:

- {'role': 'hurricanehrndz.pyenv', 'when': ['run_pyenv_role|default(true)'], 'tags': ['pyenv-dependency', 'dependencies']}
- {'role': 'hurricanehrndz.fnm', 'when': ['run_fnm_role|default(true)'], 'tags': ['nodejs-dependency', 'dependencies']}
- {'role': 'hurricanehrndz.rustup', 'when': ['run_rustup_role|default(true)'], 'tags': ['rustup-dependency', 'dependencies']}

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://buluma.github.io/) for further information.

Here is an overview of related roles:

![dependencies](https://raw.githubusercontent.com/buluma/ansible-role-nvim/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/buluma):

|container|tags|
|---------|----|
|[Ubuntu](https://hub.docker.com/r/buluma/ubuntu)|all|
|[Debian](https://hub.docker.com/r/buluma/debian)|all|
|[Fedora](https://hub.docker.com/r/buluma/fedora)|all|
|[Archlinux](https://hub.docker.com/r/buluma/archlinux)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/buluma/ansible-role-nvim/issues)

## [Changelog](#changelog)

[Role History](https://github.com/buluma/ansible-role-nvim/blob/master/CHANGELOG.md)

## [License](#license)

[Apache-2.0](https://github.com/buluma/ansible-role-nvim/blob/master/LICENSE)

## [Author Information](#author-information)

[Shadow Walker](https://buluma.github.io/)

