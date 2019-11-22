"""
Compile and save the resulting output as an image.
"""
import os
import shutil
import subprocess

from PIL import Image, ImageDraw

from autoce import find


def execution(target_directory: str) -> None:
    """
    Compile all `.c` files in the target directory and run `.out` file.

    Args:
        target_directory (str): The path where the directory to be created is placed. Example: `~ / Desktop`

    Raises:
        Exception: [description]
    """
    c_file_list = find.find_c_file(target_directory)
    execution_directory = find.find_dir(target_directory)
    os.chdir(target_directory)
    for c_file_path in c_file_list:
        print(f'c_file path: {c_file_path}')
        is_success = subprocess.check_call(['gcc', c_file_path])
        if is_success != 0:
            print('=' * 80)
            raise Exception('gcc compilation failed.')
        compile_path = os.path.join(execution_directory, 'a.out')
        if os.path.isfile(compile_path):
            os.remove(compile_path)

        compile_path = shutil.move(os.path.join(target_directory, 'a.out'), execution_directory)
        output_log = output_program(compile_path)
        create_image(output_log, execution_directory, c_file_path)


def output_program(compile_path: str) -> str:
    """
    Run the compiled file.

    Args:
        compile_path (str): Compiled `a.out` path.

    Returns:
        str: Output result.
    """
    output_log = subprocess.check_output(compile_path).decode('utf-8')
    print(f'`a.out` file path: {compile_path}')
    print('-' * 80)
    print(output_log)
    print('-' * 80)

    return output_log


def create_image(output_log: str, save_dir: str, file_name: str) -> None:
    """
    The argument string is saved in the image format of `.png`.

    Args:
        output_log (str): A string to write to the image.
        save_dir (str): Directory path for saving the generated image file.
        file_name (str): The name of the image file to save.
    """
    image_path = os.path.join(save_dir, f'{file_name}.png')
    image = Image.new('RGB', (500, 1000))
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), output_log)
    image.save(image_path)
