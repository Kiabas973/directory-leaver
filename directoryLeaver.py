import os
import shutil

folder_path = os.getcwd()
for path, dirs, files in os.walk(folder_path):
    for filename in files:
        filename_path = (path+"\\"+filename)
        if ".mp4" in filename_path or ".mkv" in filename_path in filename_path:
            shutil.move(filename_path, folder_path)
            print(filename_path)
