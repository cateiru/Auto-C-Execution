import os
import subprocess

from autoce import create


def test_exe():
    c_dir = subprocess.check_output(['pwd']).decode('utf-8')
    c_dir = os.path.join(c_dir[:-1], 'test')
    assert create.execution(c_dir) is None


def test_determine_image_size():
    log = 'HelloWorld\nHelloWorld\nHelloHelloWorld\n'
    assert create.determine_image_size(log) == (3, 15)
