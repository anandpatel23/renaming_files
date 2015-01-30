# Author: Anand Patel (23anandpatel23@gmail.com)
# Purpose: handy set of statements for renaming files in a directory

import os
import sys

def main():
    # Location of Folder
    dataLocation = raw_input("Location of data: ")
    inputExtension = raw_input("Existing extension: ")
    outputExtension = raw_input("Requested extension: ")

    # Iterates through files and replaces extensions
    for filename in os.listdir(dataLocation):
            infilename = os.path.join(dataLocation,filename)
            if not os.path.isfile(infilename): continue
            oldbase = os.path.splitext(filename)
            # Change extension here here (.org -> .org.txt, .org -> .txt, etc.)
            newname = infilename.replace(inputExtension, outputExtension)
            # Rename in OS
            output = os.rename(infilename, newname)

if __name__ == '__main__':
    main()
