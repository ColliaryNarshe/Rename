# August 2021, November 2022

from os import rename, listdir, path
from sys import exit
from colorama import Fore, init
init(autoreset=True)

folder_dir = '.\\'
show_numbers = False
removed_files = []

def rename_files(filenames, old_pattern, new_pattern, dots=False):
    for f in filenames:
        if dots:
            f, extension = path.splitext(f)
            if f.startswith('.'):
                continue
        if old_pattern in f:
            new = f.replace(old_pattern, new_pattern)
            if dots:
                new = new + extension
                f = f + extension
            rename(path.join(folder_dir, f), path.join(folder_dir, new))
            print(path.join(folder_dir, f))
            print('    ->', path.join(folder_dir, new))
    input("Process done. ")

while True:
    # Get and print filenames
    temp_files = listdir(folder_dir)
    files = []
    for idx, file in enumerate(temp_files[:]):
        if idx in removed_files:
            continue
        else:
            files.append(file)

        if show_numbers:
            print(Fore.RED + str(idx) + '. ' + file)
        else:
            print(Fore.RED + file)

    print("\nOptions: dots, between, chdir, ?, q")


    # First input
    pattern = input("Text to change: ")

    # Remove files from list.
    if pattern.startswith('rm'):
        try:
            num = int(pattern[2:])
        except ValueError:
            input("Incorrect usage of rm. eg: 'rm 7'")
        removed_files.append(num)
        continue

    # Cases:
    match pattern.lower():
        # Exit:
        case '' | 'exit' | 'q':
            exit()

        # Keywords info:
        case '?':
            print(Fore.GREEN + "\ndots: Delete all periods from each filename, except extension.\n"
                  "between: Delete all characters between two given patterns.\n"
                  "chdir: Change directory.\n"
                  "shownums: Toggle numbers.\n"
                  "rm #: Remove the file at index #.\n"
                  "q/exit: Quit.\n")
            input()

        # Remove all dots except file extension
        case 'dots':
            rename_files(files, '.', ' ', dots=True)

        # Between: Delete characters between two inputs:
        case 'between':
            left = input("Left marker: ")
            right = input("Right marker: ")
            for file_name in files:
                if left in file_name and right in file_name:
                    idx1 = file_name.index(left)
                    idx2 = file_name.index(right)
                    new_file_name = file_name[:idx1] + left + file_name[idx2:]
                    rename(path.join(folder_dir, file_name), path.join(folder_dir, new_file_name))

        # Change working directory
        case 'chdir':
            new_dir = input("New directory path: ")
            if path.exists(new_dir):
                folder_dir = new_dir
                input("Path changed successfully.")
            else:
                input("Path doesn't exist.")

        # Toggle numbering the filenames
        case 'shownums':
            show_numbers = not show_numbers

        # Rename pattern:
        case _:
            replacement = input("Change to: ")
            rename_files(files, pattern, replacement)
