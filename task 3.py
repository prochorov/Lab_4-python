import os


def show_all_files(dir_path: str, level=0):
    files = os.listdir(dir_path)
    for file in files:
        file_path = dir_path + "/" + file
        print(f'|-{level * "-" * 4} {file}')
        if os.path.isdir(file_path):
            show_all_files(file_path, level + 1)


def run():
    dir_path = "D:/институт/Питон/Lab_4/Directories"
    show_all_files(dir_path=dir_path)