# Auto-C-Execution

![3.6](https://img.shields.io/badge/Python-3.6-brightgreen)
![size](https://img.shields.io/github/repo-size/yuto51942/Auto-C-Execution)
![lastcommit](https://img.shields.io/github/last-commit/yuto51942/Auto-C-Execution)
![twitter](https://img.shields.io/twitter/follow/cateiru?style=social)


## languages

[Japanese](other/README_jp.md)

## Description

We will help you create programs in C language classes such as universities and high schools.

## Operating environment

Mac OS only.

## Details

* Necessary software fair. Install automatically if does not exist.
* `gcc` automatically compiles programs written in C.
* If it compiles normally, execute `.out`.
* If the execution is successful, the result log will be output as an image.

## Caution

* Multiple file compilation is not supported.
* If there is an input, the previous output is not displayed on the terminal.

## How to use

1. Install from Github repository using pip.

    ```bash
    pip install git+https://github.com/yuto51942/Auto-C-Execution
    ```

2. Download `main.py` from this repository, or copy and paste the code below to create a new file.
3. Change to the directory containing `.c` and move` main.py` there.
4. Change to that directory in Terminal.
5. Run that `main.py`.

    ```bash
    # Check installation of Homebrew and gcc. Install it if it is not on your PC.
    python main.py --install

    # Compile and image the result.
    python main.py --create
    ```

## `main` source code

```py
import sys
import os
from autoce import create, check


def main(args: list) -> None:
    if args[1] == '--install':
        check.brew_install()
        check.gcc_install()
        return
    elif args[1] == '--create':
        create.execution(os.getcwd())


if __name__ == "__main__":
    main(sys.argv)
```

## About static analysis and testing

* Based on Google Python Style Guide.
* I am developing at TDD. To run the test, type `tox` in Terminal.

## Change log

### v1.2.0

* The image size is changed according to the output result.

![follow](https://img.shields.io/github/followers/yuto51942?label=Follow&style=social)
