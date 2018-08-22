import os


def create_dirs(path):
    full_path = os.path.abspath(os.path.expanduser(path))

    dir_path = full_path if not os.path.isfile(full_path) \
        else os.path.dirname(full_path)

    os.makedirs(dir_path, exist_ok=True)
