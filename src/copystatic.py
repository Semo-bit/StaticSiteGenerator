import os
import shutil


from os.path import isfile
def copy_files_recursively(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)

    for file_name in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, file_name)
        dest_path = os.path.join(dest_dir_path, file_name)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursively(from_path, dest_path)



