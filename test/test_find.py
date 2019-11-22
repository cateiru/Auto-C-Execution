import os
import subprocess

from autoce import find


def test_find_c_file():
    os.chdir('../')
    c_dir = subprocess.check_output(['pwd']).decode('utf-8')
    c_dir = os.path.join(c_dir[:-1], 'test')
    test_c_file = os.path.join(c_dir, 'test.c')
    if not os.path.isfile(test_c_file):
        with open(test_c_file, 'w') as f:
            f.write('#include <stdio.h>\nint main() { printf("HelloWorld.\\n"); }\n')
    assert find.find_c_file(c_dir) is not None
