from pathlib import Path

def ListFiles():
    temp = Path("test_folder")
    for item in temp.iterdir():
        if item.is_file():
            extension = item.suffix if item.suffix else "(none)"
            print(f"{item.name} -> {extension}")
        


ListFiles()