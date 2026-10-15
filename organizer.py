from pathlib import Path
import argparse
def ListFiles(folder):
    temp = Path(folder)
    for item in temp.iterdir():
        if item.is_file():
            extension = item.suffix if item.suffix else "(none)"
            print(f"{item.name} -> {extension}")
        

parser = argparse.ArgumentParser(description="Organizer files by file type")
parser.add_argument("folder", help="Folder to organize")
args = parser.parse_args()

ListFiles(args.folder)