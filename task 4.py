import os
import pathlib


result = []


def find_all_files_by_suffix(dir_path: str, suffix: str):
    files = os.listdir(dir_path)
    for file in files:
        file_path = dir_path + "/" + file
        file_suffix = pathlib.Path(file_path).suffix
        if file_suffix == suffix:
            result.append(file_path)
        if os.path.isdir(file_path):
            find_all_files_by_suffix(file_path, suffix)


def run():
    dir_path = "D:/институт/Питон/Lab_4/Directories"
    extension = ".py"
    find_all_files_by_suffix(dir_path=dir_path, suffix=extension)
    print(*result, sep="\n")


run()