import os
import sys

# Simple File Explorer in Python!

# Main function "The Navigator"


def navigator(start):
    counter = 0
    filelist = []
    print('++++++++++++ Current Directory ++++++++++++')
    print(start.upper().center(20, "-"))
    for files in os.listdir(os.path.join(start)):
        print(f'{counter}-{files}')
        counter += 1
        filelist.append(files)
    print("(A) atras| (H) Historial | (E) Exit")
    wtd = input("#> ")
    if wtd.lower() == "a":
        return back(start)
    if wtd.lower() == "e":
        sys.exit()

    if wtd.lower() == "h":
        return navigator(start)
    # check if the selected file is either a file or a directory
    if os.path.isdir(os.path.join(start, filelist[int(wtd)])):
        changedir(os.path.join(start, filelist[int(wtd)]))
    # check if the selected file is either a file or a directory
    if not os.path.isdir(os.path.join(start, filelist[int(wtd)])):
        file_menu(os.path.join(start, filelist[int(wtd)]))

# funtion to do chang dir


def changedir(directory):
    os.chdir(directory)
    return navigator(directory)

# File menu


def file_menu(file):
    print("""
    
    - (O) Open the file
    - (D) Delete the file
    - (R) Rename file
    - (B) Back to navigator
    
    """)
    wtd = input("#> ")
    if wtd.lower() == "o":
        with open(file) as f:
            print('--------file content--------')
            print(f.read())
            print('--------end file content--------')

    elif wtd.lower() == "d":
        os.remove(file)

    elif wtd.lower() == "b":
        pass

    elif wtd.lower() == "r":
        name = input("New name: ")
        os.rename(file, (os.path.dirname(file) + "\\" + name))

    return changedir(os.path.dirname(file))


# Go back function!!!!


def back(directory):
    cwd = directory.split("\\")
    if len(cwd) >= 1:
        cwd.pop()

    if len(cwd) == 1:
        cwd.append("\\")

    newpath = "\\".join(cwd)
    return navigator(newpath)


dir = input('Digita el directorio completo: ')
navigator(dir)
