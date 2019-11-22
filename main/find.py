"""
gcc execution
"""
import glob
import os


def find_dir(target_directory: str) -> str:
    """
    Create a directory to put programs written in C.

    Args:
        target_directory (str): The path where the directory to be created is placed. Example: `~ / Desktop`

    Returns:
        str: The path of the created directory.
    """
    execution_directory = os.path.join(target_directory, 'c_execution')
    if not os.path.isdir(execution_directory):
        os.makedirs(execution_directory)

    return execution_directory


def find_c_file(execution_directory: str) -> list:
    """
    Returns a list of paths of `.c` files in the argument directory.

    Args:
        execution_directory (str): The directory to look for.

    Returns:
        list: A list containing the file path of `.c`.

    Raises:
        Exception: Could not find file containing `.c`.
    """
    c_file_path = os.path.join(execution_directory, '*.c')
    c_file_list = glob.glob(c_file_path)
    if c_file_list is None:
        raise Exception('Could not find file containing `.c`.')
    return c_file_list
