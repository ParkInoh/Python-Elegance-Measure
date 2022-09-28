import os


# import constants


# def camel_to_snake(name) -> str:
#     """
#     Converts a camel case name to snake case.
#
#     :param name: str
#     :return: str
#     """
#     name = constants.REGEX_CAMEL_TO_SNAKE1.sub(r'\1_\2', name)
#     name = constants.REGEX_CAMEL_TO_SNAKE2.sub(r'\1_\2', name)
#     name = name.replace("-", "_").lower()
#     return name


def get_files_by_dir(dir_path: str = './public/') -> list[str]:
# def get_files_by_dir(dir_path: str = './') -> list[str]:
    """
    Returns the file paths in a directory.

    :param dir_path: str: directory path
    :returns: list[str]
    """
    assert os.path.isdir(dir_path), 'dir_path must be a directory'
    return [[file for file in files] for _, _, files in os.walk(dir_path)][0]


def get_codes(files: list[str]) -> list[str]:
    """
    Returns the codes in a list of files.

    :param files: list[str]
    :returns: list[str]
    """
    assert len(files) > 0, 'length of files must be greater than 0'
    codes = []
    for file in files:
        data = open('./public/' + file, 'rt', encoding='UTF8')
        # data = open(file, 'rt', encoding='UTF8')
        codes.append(data.read())
        data.close()
    return codes
