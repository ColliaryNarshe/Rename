# August 2021

from glob import glob
import os
from sys import exit

while True:

    for item in os.listdir():
        print(item)

    files = glob('./*')

    pattern = input("Text to change: ")
    if not pattern:
        exit()
    replacement = input("Change to: ")

    for f in files:
        if pattern in f:
            new = f.replace(pattern, replacement)
            os.rename(f, new)
