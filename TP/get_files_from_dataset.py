import os

def get_files_from_dataset():
    path = "./dataset"
    dir_list = list(map(lambda path: "./dataset/" + path, os.listdir(path)))
    return dir_list