import os
import shutil
def sort(data_folder : str) -> None:
    """get only pdf files to avoid errors and place it in a separate folder (sorted_data)"""
    data_path = data_folder
    destination_folder = "sorted_data"
        
    for filename in os.listdir(data_path):
    
        file_path = file_path = os.path.join(data_path, filename)
        if os.path.isfile(file_path) and get_file_extension(file_path) == "pdf":
            shutil.copy2(file_path, os.path.join(destination_folder, filename + ".pdf"))


def get_file_extension(file_path :str) -> str:
    """returns the file extension"""
    return file_path.split(".")[-1]