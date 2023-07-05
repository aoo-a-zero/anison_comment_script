[日本語](README.ja.md)

# anison_comment_script

This Python script automatically adds anime song information to the comment field for all songs registered in your iTunes (Music) library. It uses various csv data files provided by [AnisonGeneration](http://anison.info/), which can be found on their [download page](http://anison.info/data/download.html).

# Environment Tested

- macOS 13
- Python 3.11.3
- Music 1.3.5.8 (ja)

# Usage

1. Install python and related tools

```bash
pip install regex jaconv appscript
```

2. Place the csv files provided by [AnisonGeneration](http://anison.info/) as follows:

```
anison_comment_script
├── anison_comment.py
├── anison.csv
├── game.csv
└── sf.csv
```

3. Execute the script

```bash
python anison_comment.py 
```

If it doesn't run successfully, try granting Python "Full Disk Access" permissions.

# Specifications

The script normalizes the title and artist names on both the csv and iTunes (Music) side and determines if they match. If the song title and artist name match, it registers the show name in the comments field.

The conditions for a match are as follows:
- If the csv name or iTunes (Music) name is 3 characters or less, it's a match if they are exactly the same.
- If the csv name or iTunes (Music) name is 4 characters or more, it's a match if one string contains the other.

The script also includes a process for handling multiple artist name notations and aliases. Please refer to the code for more details.

# Notes

- This script is designed not to overwrite comments, but as a precaution, please take a backup before running it.
  - We do not take any responsibility for troubles, losses, or damages caused by running this script.
- Due to the script's specifications, unintended show names may get registered.
  - ex) `Release Tha Power / M-PROJECT` = `POWER / JAM Project` (Even though unrelated, they are misjudged as the same song because each contains the other's string).
  - If you have a better matching condition, we are waiting for your Pull Request.

# License

[THE BEER-WARE LICENSE](https://en.wikipedia.org/wiki/Beerware)

> If we meet some day, and you think this stuff is worth it, you can buy me a beer in return.

🍺🐟