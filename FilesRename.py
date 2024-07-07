import os
import sys
import click

def GetFiles(mainPath: str, addedStr: str):
    files = os.listdir(mainPath)
    if (click.confirm(f"Do you want to rename {len(files)} files?", True)):
        files = CreateFullFileNames(mainPath, files)
        RenameFiles(files, addedStr)
    else:
        print("Renaming canceled")

def CreateFullFileNames(path: str, files: list[str]):
    for i in range(len(files)):
        files[i] = os.path.join(path, files[i])
    return files

def RenameFiles(files: list[str], addedStr: str):
    for file in files:
        fileNameParts = os.path.splitext(file)
        newFileName = fileNameParts[0] + addedStr + fileNameParts[1]
        os.rename(file, newFileName)
    print("Files were renamed")
         

def Main():
    addedStr = "_1"

    if(len(sys.argv) >= 2):
        GetFiles(sys.argv[1], addedStr)
    else:
        GetFiles(input("Enter the path of the work catalog: "), addedStr)

if __name__ == "__main__":
	Main()