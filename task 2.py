import os


def return_directory_info(dir_name: str) -> (list, list):
    objects = os.listdir(dir_name)
    files, dirs = [], []
    for obj in objects:
        is_folder = os.path.isdir(dir_name + "/" + obj)
        if is_folder:
            dirs.append(obj)
        else:
            files.append(obj)
    return files, dirs


def run():
    dir_name = "../"
    files, dirs = return_directory_info(dir_name=dir_name)
    print(f"{files=}\n{dirs=}")


run()