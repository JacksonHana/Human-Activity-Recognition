import os

# Specify the directory you want to scan
directory_path = "./UCF50"

# Get all folder names in the directory
folder_names = [name for name in os.listdir(directory_path)
                if os.path.isdir(os.path.join(directory_path, name))]

print(folder_names)
