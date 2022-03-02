"""
This module collects .xyz files from a selected directory
"""
import os

def xyz_reader():
    print("Paste directory path where coordinates are located:")
    directory = input("directory = ") #fix by removing "
    directory = directory.strip('"')
    
    sorted_files = sorted(os.listdir(directory))
    
    print("Coordinate files in your directory: ")
    for file in sorted_files:
        if file.endswith(".xyz"):
            print(file)


if __name__ == "__main__":
    xyz_reader()
