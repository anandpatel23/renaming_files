# Author: Anand Patel (23anandpatel23@gmail.com)
# Purpose: handy set of statements for renaming files in a directory

import os
import sys

def main():
    # Location of Folder
    dataLocation = raw_input("Location of data: ")

    # Iterates through files and replaces extensions

   # for dirname, dirnames, filenames in os.walk(dataLocation):
    for filename in os.listdir(dataLocation):
            infilename = os.path.join(dataLocation,filename)
            if not os.path.isfile(infilename): continue
            oldbase = os.path.splitext(filename)
            # Change extension here here (.org -> .org.txt, .org -> .txt, etc.)
            newname = infilename.replace('.org', '.csv')
            # Rename in OS
            output = os.rename(infilename, newname)

if __name__ == '__main__':
    main()
