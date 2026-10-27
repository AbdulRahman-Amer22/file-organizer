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
    target = get_unique_path(destination, item.name)
    if dry_run:
        print(f"Would move {item.name} -> {category} / {target.name}")
    else:
        destination.mkdir(exist_ok=True)
        shutil.move(str(item), str(target))
        print(f"Moved {item.name} -> {category} / {target.name}")


def organize(folder, dry_run):
    for item in list(folder.iterdir()):
        if item.is_file():
            try: 
                    move_file(item, folder, dry_run)
            except OSError as e:
                print(f"Could not move {item.name}: {e}")




    
def get_unique_path(destination, file_name):
    file_name = Path(file_name)
    stem = file_name.stem
    suffix = file_name.suffix
    candidate = destination / file_name
    i = 0   
    while candidate.exists():
        i +=1
        candidate = destination / f"{stem}_{i}{suffix}"
    return candidate



def main():
    parser = argparse.ArgumentParser(description="Organize files by file type")
    parser.add_argument("folder", help="Folder to organize")
    parser.add_argument("--dry-run", action="store_true", help="show what would happen without moving files")
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.exists():
        parser.error(f"'{folder}' does not exist")
    if not folder.is_dir():
        parser.error(f"'{folder}' is not a folder")

    organize(folder, args.dry_run)   

if __name__ == "__main__":
    main()