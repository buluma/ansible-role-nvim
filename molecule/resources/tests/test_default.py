import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize("pattern", [
  "source /home/hurricanehrndz/.local/share/pyenv/pyenvrc",
  "export FNM_DIR=/home/hurricanehrndz/.local/share/fnm",
  "export PATH=/home/hurricanehrndz/.local/bin",
  "fnm env",
  'source /home/hurricanehrndz/.rustrc',
  'source ~/.fzf.bash'
])
def test_bashrc(host, pattern):
    f = host.file('/home/hurricanehrndz/.bashrc')

    assert f.contains(pattern)


@pytest.mark.parametrize("command", [
    "cd $HOME;fnm --version",
    "cd $HOME;npm --version",
    "cd $HOME;fzf --version",
    "cd $HOME;rustup --version",
    "cd $HOME;pyenv --version"
])
def test_npm(host, command):
    user_home = "/home/hurricanehrndz"
    bash_command = f"HOME={user_home} bash -i -c '{command}'"
    with host.sudo('hurricanehrndz'):
        assert host.check_output(
           bash_command
        ) != ""
