import os

working_dir = os.getcwd()


def get_relative_path(folder: str, csvfilename: str) -> str:
    """Returns the path of the file
    """
    return os.path.join(working_dir, folder, csvfilename)
