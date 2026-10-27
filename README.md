# File Organizer


A command line tool that sorts files into folders by type


- Sorts files by file type (images, videos, documents, other)
- `--dry-run` previews moves without touching anything 
- Overwriting protection, if file name collision occurs, creates new file name to avoid overwriting 
- Error handling, an error moving a file doesn't stop the rest

Tested with Python 3.15

No third party dependencies 

## Installation 

- Clone the repo git 
- Move into the folder 
``` bash
clone https://github.com/AbdulRahman-Amer22/file-organizer.git
cd file-organizer
```
## Usage

- To organize a folder use
`python organizer.py <folder>`
- To preview organization use 
`python organizer.py <folder> --dry-run`

- sample output

```
Moved clip4.mp4 -> Videos / clip4.mp4
Moved data.csv -> Documents / data.csv
Moved LICENSE -> Other / LICENSE
Moved Makefile -> Other / Makefile
Moved notes1.txt -> Documents / notes1.txt
Moved notes2.txt -> Documents / notes2.txt
Moved notes3.txt -> Documents / notes3.txt
Moved notes4.txt -> Documents / notes4.txt
...
```

## Limitations
 
- only organizes files in the folder (no subfolders)
- no undo functionality to reverse changes  