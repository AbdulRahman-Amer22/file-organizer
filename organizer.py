from pathlib import Path
import argparse

CATEGORIES = {

    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".csv": "Documents",
    ".mp4": "Videos",
    
}

def get_category(item):
    extension = item.suffix.lower()
    return CATEGORIES.get(extension, "Other" )


def list_files(folder):
    temp = Path(folder)
    for item in temp.iterdir():
        if item.is_file():
            extension = item.suffix if item.suffix else "(none)"
            print(f"{item.name} -> {extension}")



parser = argparse.ArgumentParser(description="Organizer files by file type")
parser.add_argument("folder", help="Folder to organize")
args = parser.parse_args()

list_files(args.folder)