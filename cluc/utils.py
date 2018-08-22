import os


def create_dirs(path):
    full_path = os.path.abspath(os.path.expanduser(path))

    if full_path.endswith('/'):  # it's definitely a directory
        dir_path = full_path
    else:
        # path to a file provided, so create a directory container for it
        dir_path = os.path.dirname(full_path)

    os.makedirs(dir_path, exist_ok=True)
