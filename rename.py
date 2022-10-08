# August 2021

from glob import glob
import os
from sys import exit
from os import path
from colorama import Fore, init
init(autoreset=True)

def rename_files(filenames, old_pattern, new_pattern, dots=False):
    for f in filenames:
        if old_pattern in f:
            if dots:
                filename, extension = path.splitext(f)
            else:
                filename = f
            new = filename.replace(old_pattern, new_pattern)
            if dots:
                new = new + extension
            os.rename(f, new)



while True:
    # Get and print filenames
    for item in os.listdir():
        print(Fore.RED + item)
    print("\nOptions: dots, between, ?, q")
    files = glob('*')  # ./*

    # First input
    pattern = input("Text to change: ")
    # ? Info
    if pattern == "?":
        print(Fore.GREEN + "\ndots: Delete all periods from each filename, except extension.\n"
              "between: Delete all characters between two given patterns.\n"
              "q/exit: Quit.\n")
        input()
        continue
    # Exit
    if not pattern or pattern.lower() == "exit" or pattern.lower() == 'q':
        exit()
    # Remove all dots except file extension
    if pattern.lower() == "dots":
        rename_files(files, '.', '', dots=True)
        continue
    # Between: Delete characters between two inputs:
    if pattern.lower() == 'between':
        left = input("Left marker: ")
        right = input("Right marker: ")
        for file_name in files:
            if left in file_name and right in file_name:
                idx1 = file_name.index(left)
                idx2 = file_name.index(right)
                new_file_name = file_name[:idx1] + left + file_name[idx2:]
                print(new_file_name)
                os.rename(file_name, new_file_name)
        continue

    # Second input
    replacement = input("Change to: ")

    rename_files(files, pattern, replacement)
