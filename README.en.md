[日本語](README.md)

# anison_comment_script

This is a Python script that automatically adds anime song information to the comment section for all songs registered in the Music (iTunes) library.
It utilizes the [various csv data](http://anison.info/data/download.html) published by [AnisonGeneration](http://anison.info/).

# Verified Operating Environment

- macOS 13
- Python 3.11.3
- Music(iTunes) 1.3.5.8 (ja)

# Usage

1. Install python and related tools.

```bash
pip install regex jaconv appscript
```

2. Place [the various csv data](http://anison.info/data/download.html) distributed by [AnisonGeneration](http://anison.info/) as follows:

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

If you are unable to execute the script successfully, please try granting Python "Full Disk Access" permissions.

# Specifications

The script normalizes the titles and artist names on the csv and Music (iTunes) sides, then determines whether they match.
If both the song name and artist name match, the program name will be registered in the comment section.

The conditions for a match are as follows:
- If either the csv or Music (iTunes) is 3 characters or less, it's a match if they are exactly the same.
- If either the csv or Music (iTunes) is 4 characters or more, it's a match if one string contains the other.

Furthermore, the script includes processing to consider multiple notations or aliases for artist names.

Please check the [code within the script](anison_comment.py) for details.

# Caution

- We are not responsible for any troubles, losses, or damages caused by executing this script.
  - We have taken into account not to overwrite comments, but please take a backup just in case.
- Due to the nature of the script, unintended program names may be registered.
  - ex) `Release Tha Power / M-PROJECT` = `POWER / JAM Project`  
    (They are mistakenly identified as the same song because they contain each other's strings, despite being unrelated.)
  - If you have a better matching condition, please send a Pull Request.

# License

[THE BEER-WARE LICENSE](https://en.wikipedia.org/wiki/Beerware)

> If we meet some day, and you think this stuff is worth it, you can buy me a beer in return.

🍺🐟
