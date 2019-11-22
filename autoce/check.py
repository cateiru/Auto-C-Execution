"""
Check the necessary software.
"""
import subprocess


def brew_install() -> None:
    """
    Install homebrew.
    Passed if already installed.

    Raises:
        Exception: Homebrew installation failed.
    """
    try:
        subprocess.check_call(['xcode-select', '--install'])
    except subprocess.CalledProcessError:
        pass
    brew_check = subprocess.check_output(['brew', '--version'])
    if brew_check[:8] == b'Homebrew':
        print('Homebrew installed.')
        return
    brew_install_link = '/usr/bin/ruby -e "$(curl -fsSL\
                         https://raw.githubusercontent.com/Homebrew/install/master/install)"'
    is_success = subprocess.check_call(brew_install_link.split())
    if is_success != 0:
        raise Exception('Homebrew installation failed.')


def gcc_install() -> None:
    """
    Install gcc. Pass if it already exists.

    Raises:
        Exception: gcc installation failed.
    """
    gcc_check = subprocess.check_output(['brew', 'list']).decode('utf-8')
    if 'gcc' in gcc_check:
        print('gcc installed.')
        return
    is_success = subprocess.call(['brew', 'install', 'gcc'])
    if is_success != 0:
        raise Exception('gcc installation failed.')
