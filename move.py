import glob
import os

parent_directory_name = ""

os.rename(parent_directory_name, parent_directory_name.replace(" ", "").replace("　", ""))
parent_directory_name = parent_directory_name.replace(" ", "").replace("　", "")
directories = glob.glob(f"./{parent_directory_name}/*")

if not directories:
    print("error!: not exist such directory")
    
for directory in directories:
    directory_old = directory
    directory = directory.replace(" ", "")
    os.rename(directory_old, directory)
    
    print(f"directory : {directory}")
    print(f"path : {directory}/*")
    
    for file in glob.glob(f"{glob.escape(directory)}/*"):
        file_new = file[::-1].replace("/", "_", 1)[::-1]
        os.rename(file, file_new)
    print(directory)
    os.rmdir(directory)
        