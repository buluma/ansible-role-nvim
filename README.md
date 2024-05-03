# hurricanehrndz.nvim

[![Build Status][action-badge]][action-link]
[![Galaxy Role][role-badge]][role-link]
[![MIT licensed][mit-badge]][mit-link]

Ansible role to install my [Neovim configuration][nvim-config].

## Requirements

None.

## Role Variables

A description of the settable variables for this role are listed below,
including any variables that are in [defaults/main.yml](defaults/main.yml),
[vars/main.yml](vars/main.yml), and any variables that can/should be set via
parameters to the role.

```yaml
nvim_user: "{{ ansible_user | default(lookup('env', 'USER')) }}"
```

The user for whom the Neovim runtime configuration and all its dependencies will
get installed for, default is `ansible_user`.

```yaml
nvim_git_repo: "https://github.com/hurricanehrndz/nvim"
```

URL to git repository containing Neovim runtime configuration to be installed.

```yaml
nvim_python_ver: 3.8.0
```

Python version to install via `pyenv` dependency, as to provide support for python
based plugins within Neovim.

```yaml
nvim_python_mods:
  - pynvim
  - neovim-remote
  - vim-vint
  - flake8
  - yamllint
  - jedi
  - ansible
  - testinfra
  - docker
  - molecule
```

`nvim_python_mods` is a list of python modules to be installed for support of
completions engines and various other Neovim features. At a minimum, list
should contain `pynvim`.

```yaml
nvim_fzf_bin_only: false
```

Set to `true`, to suppress modifications to `nvim_user`'s runtime
shell configuration during fzf installation.

```yaml
nvim_fnm_root_suffix: ".local/share/fnm"
```

Install destination for `fnm` within `nvim_user`'s home directory.
Defaults to `.local/share/fnm`.

```yaml
nvim_pyenv_root_suffix: ".local/share/pyenv"
```

Install destination for `pyenv` within `nvim_user`'s home directory.
Defaults to `.local/share/pyenv`.

```yaml
nvim_nodejs_version: "latest-v12.x"
```

nodejs version to install.

```yaml
nvim_npm_global_pkgs: []
```

List of npm global packages to install, default includes `neovim` only.

## Dependencies

- hurricanehrndz.pyenv
- hurricanehrndz.fnm
- hurricanehrndz.rustup

## Example Playbook

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```yaml
- name: Install neovim configuration
  hosts: all
  vars:
    nvim_user: hurricanehrndz
  tasks:
    - name: Update repo cache
      action: >
        {{ ansible_pkg_mgr }} update_cache=yes

    - name: Add hurricanehrndz user
      user:
        name: "{{ nvim_user }}"
        create_home: yes
        shell: /bin/bash

    - name: Run nvim role
      include_role:
        name: ansible-nvim
```

## License

[MIT](LICENSE)

## Author Information

[Carlos Hernandez aka HurricaneHrndz](https://github.com/hurricanehrndz)

[nvim-config]: https://github.com/hurricanehrndz/nvim
[role-badge]: https://img.shields.io/ansible/role/d/46776?style=for-the-badge
[role-link]: https://galaxy.ansible.com/hurricanehrndz/nvim/
[mit-badge]: https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge
[mit-link]: https://raw.githubusercontent.com/hurricanehrndz/ansible-nvim/master/LICENSE
[action-badge]: https://img.shields.io/github/workflow/status/hurricanehrndz/ansible-nvim/CI?style=for-the-badge
[action-link]: https://github.com/hurricanehrndz/ansible-nvim/actions?query=workflow%3ACI
