"""
Determine and set the directory for `.c` files.
"""
import glob
import os
import pathlib
import shutil


def find_dir(target_directory: str) -> str:
    """
    Create a directory to place the program written in C, and copy `.c` to that directory.

    Args:
        target_directory (str): The path where the directory to be created is placed. Example: `~ / Desktop`

    Returns:
        str: The path of the created directory.
    """
    execution_directory = os.path.join(target_directory, 'c_execution')
    if not os.path.isdir(execution_directory):
        os.makedirs(execution_directory)

    c_file_path = os.path.join(target_directory, '*.c')
    c_file_list = glob.glob(c_file_path)
    if c_file_list is not None:
        for path in c_file_list:
            try:
                shutil.copy(path, execution_directory)
            except shutil.Error:
                pass
    return execution_directory


def find_c_file(target_directory: str) -> list:
    """
        Create a directory to put programs written in C, copy `.c` to that directory, and
        Returns a list of paths of `.c` files in the argument directory.

    Args:
        target_directory (str): The path where the directory to be created is placed. Example: `~ / Desktop`

    Returns:
        list: A list containing the file path of `.c`.

    Raises:
        Exception: Could not find file containing `.c`.
    """
    execution_directory = find_dir(target_directory)
    c_file_list = list(pathlib.Path(execution_directory).glob('*.c'))
    if c_file_list is None:
        raise Exception('Could not find file containing `.c`.')
    return c_file_list
