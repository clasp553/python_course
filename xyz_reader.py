"""
This module collects .xyz files from a selected directory
"""
import os

def xyz_reader():
    print("Paste directory path where coordinates are located:")
    directory = input("directory = ")
    directory = directory.strip('"')
    
    sorted_files = sorted(os.listdir(directory))
    
    print("\nCoordinate files in your directory:\n")
    for file in sorted_files:
        if file.endswith(".xyz"):
            print(file)
    
    xyzfile = input("\nSelected file: ")
    xyzfile = xyzfile+".xyz"
    print("\n" + xyzfile)
    
    charge = input("Complex charge: ")
    mult = input("Complex multiplicity: ")