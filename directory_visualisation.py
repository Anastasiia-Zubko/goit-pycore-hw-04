from colorama import Fore # type: ignore
from pathlib import Path

def print_directory(directory, increment: int = 0) -> None:
    space = '  ' * increment # create space increment to display the hierarchy of directories
    try:
        for path in directory.iterdir(): # iterate through all the files and folders in the given directory
            if path.is_dir(): # check if the object is directory
                print(f"{space}{Fore.BLUE}{path.name}/") # print directory name in blue color 
                print_directory(path,  increment + 1) # recursively call the function adding an increment to print directories inside the given directory  
            else:
                print(f"{space}{Fore.GREEN}{path.name}") # print file name in green color 
    except FileNotFoundError:
        print(Fore.RED , "Directory does not exist: " , directory) # check for error file not found 
    except Exception as error: # catch and show any other error
        print(Fore.RED + "Error: " , error) # print that error


if __name__ == "__main__":
    path = Path("/Users/anastasiiazubko/Python/goit-pycore-hw-04")
    print(f"Structure of directory with path: {path}\n")
    print_directory(path)


