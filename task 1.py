import re
import tarfile
import os
import pathlib
import shutil

current_dir = os.path.dirname(os.path.realpath(__file__))


def files_white_list(
    filenames: list[str],
    mask: str,
    white_list=None,
    root_path=None,
    unpack_dir_path=None,
):
    if white_list is None:
        white_list = []

    for filename in filenames:
        if root_path is not None:
            root_path_n = root_path + "/" + filename
        else:
            root_path_n = filename
        if len(re.findall(mask, root_path_n)) == 0:
            if root_path is not None:
                white_list.append(root_path + "/" + filename)
            else:
                white_list.append(filename)

        is_folder = os.path.isdir(filename)
        if is_folder:
            files_white_list(
                filenames=os.listdir(unpack_dir_path + "/" + filename),
                mask=mask,
                white_list=white_list,
                root_path=root_path_n,
            )
    return white_list


def unpack_tar(
    tar_name: str,
    unpack_dir_path=current_dir + "/unpack",
    copy_dir_path=current_dir + "/copy",
    mask="html",
):
    tarfile.open(name=tar_name).extractall(unpack_dir_path)  # unpacking
    files_to_create = files_white_list(
        filenames=os.listdir(unpack_dir_path),
        mask=mask,
        unpack_dir_path=unpack_dir_path,
    )
    for file in files_to_create:
        if not os.path.exists(copy_dir_path + "/" + "".join(file.split("/")[:-1])):
            os.makedirs(copy_dir_path + "/" + "".join(file.split("/")[:-1]))

        if pathlib.Path(file).suffix != "":
            shutil.copy(
                src=unpack_dir_path + "/" + file, dst=copy_dir_path + "/" + file
            )


def run():
    try:
        unpack_tar(tar_name="masterclass.tar.gz")
    except Exception as e:
        raise Exception(f"Error!\nDescription: {e}")


run()