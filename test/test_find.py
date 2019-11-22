import os
import subprocess

from main import find


def test_find_c_file():
    dir = find.find_dir(subprocess.check_output(['cd', '..', '&&', 'pwd']).decode('utf-8'))
    test_c_file = os.path.join(dir, 'test.c')
    if not os.path.isfile(test_c_file):
        with open(test_c_file, 'w') as f:
            f.write('#include <stdio.h>\nint main() { printf("HelloWorld.\\n"); }\n')
    assert find.find_c_file(dir)
