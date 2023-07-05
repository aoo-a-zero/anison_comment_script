import csv
import regex
import jaconv
import string
import unicodedata
from appscript import *

def normalize(s):
    if s:
        # Unicode 文字列の正規化
        s = unicodedata.normalize('NFKC', s)
        # Unicode の範囲で、英語、日本語の漢字・カタカナ・ひらがな以外を一括で除去
        s = regex.sub(r'[^\p{Script=Latin}\p{Script=Hiragana}\p{Script=Katakana}\p{Script=Han}\p{Number}a-zA-Z0-9]', '', s)
        # 大文字を小文字に
        s = s.lower()
        # 半角化
        s = jaconv.z2h(s, kana=True, ascii=True, digit=True)
    else:
        s = ''
    return s

def normalize_csv_artist(s):
    if s:
        input_str = s.replace('（', '(').replace('）', ')')
        splits = input_str.split('(')
        normalized_artists = []
        for split in splits:
            if split.strip():
                items = split.replace(')', '').split(',')
                normalized_items = [normalize(item.strip()) for item in items if item.strip()]
                normalized_artists.extend(normalized_items)
        return normalized_artists
    return []

def is_match(csv_data, song_data):
    if not csv_data or not song_data:
        return False
    if len(csv_data) <= 3 or len(song_data) <= 3:
        return csv_data == song_data
    else:
        return (csv_data in song_data) or (song_data in csv_data)

csv_files = ['anison.csv', 'sf.csv', 'game.csv']
csv_data = []

for csv_file in csv_files:
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if all(key in row for key in ['楽曲名', '歌手名']) and row.get('歌手名', '') != '不明':
                csv_title = normalize(row.get('楽曲名', ''))
                csv_artist = normalize_csv_artist(row.get('歌手名', ''))
                if csv_artist:
                    match = ' '.join([row.get(key, '') for key in ['番組分類', '番組名', '摘要', '放映順'] if row.get(key, '')])
                    csv_data.append((csv_title, csv_artist, match))

print("Start processing songs...")

for item in csv_data:
    print(item)

for song in app('Music').playlists['ライブラリ'].tracks.get():
    song_title = normalize(song.name.get())
    song_artist = normalize(song.artist.get())
    
    if not song_title:
        print(f"Skipped due to empty song title: {song.name.get()}, {song.artist.get()}, {song_title}, {song_artist}")
        continue
    
    existing_comment = song.comment.get()
    if existing_comment:
        print(f"Comment already exists for: {song.name.get()}, {song.artist.get()}, {song_title}, {song_artist}")
        continue

    matches = []
    for csv_title, csv_artists, match in csv_data:
        for csv_artist in csv_artists:
            if is_match(csv_artist, song_artist) and is_match(csv_title, song_title):
                if match not in matches:
                    matches.append(match)
    if matches:
        song.comment.set('、\n'.join(matches))
        print(f"Comment added for: {song.name.get()}, {song.artist.get()}, {song_title}, {song_artist}")
    else:
        print(f"No comment added for: {song.name.get()}, {song.artist.get()}, {song_title}, {song_artist}")
