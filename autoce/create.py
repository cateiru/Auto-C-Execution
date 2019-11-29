"""
Compile and save the resulting output as an image.
"""
import os
import subprocess
from math import ceil
from typing import Tuple

from PIL import Image, ImageDraw, ImageFont

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
    os.chdir(execution_directory)
    for c_file_path in c_file_list:
        print(f'c_file path: {c_file_path}')
        is_success = subprocess.check_call(['gcc', c_file_path])
        if is_success != 0:
            print('=' * 80)
            raise Exception('gcc compilation failed.')

        compile_path = os.path.join(execution_directory, 'a.out')
        output_log = _output_program(compile_path)
        _create_image(output_log, execution_directory, c_file_path)
        if os.path.isfile(compile_path):
            os.remove(compile_path)


def _output_program(compile_path: str) -> str:
    """
    Run the compiled file.

    Args:
        compile_path (str): Compiled `a.out` path.

    Returns:
        str: Output result.
    """
    output_log = subprocess.run([compile_path], stdout=subprocess.PIPE, check=True)
    print(f'`a.out` file path: {compile_path}')
    print('-' * 80)
    print(output_log.stdout.decode('utf-8'))
    print('-' * 80)

    return output_log.stdout.decode('utf-8')


def _create_image(output_log: str, save_dir: str, file_name: str) -> None:
    """
    The argument string is saved in the image format of `.png`.

    Args:
        output_log (str): A string to write to the image.
        save_dir (str): Directory path for saving the generated image file.
        file_name (str): The name of the image file to save.
    """
    image_path = os.path.join(save_dir, f'{file_name}.png')
    log_break, log_max_len = _determine_image_size(output_log)
    height = ceil(log_break*35 + 100)
    width = ceil(log_max_len*30 + 50)
    if os.path.isfile('/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc'):
        font_name = '/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc'
    else:
        font_name = '/System/Library/Fonts/Menlo.ttc'

    image = Image.new('RGB', (width, height), (22, 24, 33))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_name, 30)
    draw.text((0, 0), output_log, font=font)
    image.save(image_path)


def _determine_image_size(output_log: str) -> Tuple[int, int]:
    """
    Get the size of the output character to determine the size of the image to be created.

    Args:
        output_log (str): Log of executing `.c`.

    Returns:
        Tuple[int, int]: The number of line breaks and the maximum number of characters when a line break occurs.
    """

    line_break = output_log.count('\n')
    if line_break == 0:
        return 0, len(output_log)

    line_count = 0
    max_line = 0
    for element in output_log:
        if element == '\n':
            max_line = max(max_line, line_count)
            line_count = 0
            continue
        line_count += 1

    return line_break, max_line
