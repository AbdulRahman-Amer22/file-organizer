from pathlib import Path 

import argparse
import shutil
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


def move_file(item, folder, dry_run):
    category = get_category(item)
    destination = folder / category
    if dry_run:
        print(f"Would move {item.name} -> {category}")
    else:
        destination.mkdir(exist_ok=True)
        shutil.move(str(item), str(destination / item.name))
        print(f"Moved {item.name} -> {category}")


def organize(folder, dry_run):
    for item in list(folder.iterdir()):
        if item.is_file():
            move_file(item, folder, dry_run)
    

parser = argparse.ArgumentParser(description="Organize files by file type")
parser.add_argument("folder", help="Folder to organize")
parser.add_argument("--dry-run", action="store_true", help="show what would happen without moving files")
args = parser.parse_args()

organize(Path(args.folder), args.dry_run)   