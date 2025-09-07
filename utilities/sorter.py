import os.path
from mutagen.easyid3 import EasyID3


CURR_DIR = os.getcwd()
DL_DIR = os.path.join(CURR_DIR, "dl_dir")
DL_DIR_FILES = os.listdir(DL_DIR)


if __name__ == "__main__":
    print("Sorting files in dl_dir into artist/album folders...")

    # Process each file in dl_dir
    for file in DL_DIR_FILES:
        FILE_PATH = os.path.join(DL_DIR, file)

        # Skip if not a file
        if not os.path.isfile(FILE_PATH):
            print(f"Not a file: {FILE_PATH}")
            continue

        # Read ID3 tags
        try:
            audio = EasyID3(FILE_PATH)
            artist = audio.get("albumartist", ["Unknown Artist"])[0]
            album = audio.get("album", ["Unknown Album"])[0]
            title = audio.get("title", ["Unknown Title"])[0]
        except Exception as e:
            print(f"Skipping {FILE_PATH}: {e}")
            continue

        # Create artist/album directory structure inside dl_dir
        artist_dir = os.path.join(DL_DIR, artist)
        album_dir = os.path.join(artist_dir, album)
        if not os.path.exists(album_dir):
            os.makedirs(album_dir)

        # Move file if not already present in album_dir
        dest_path = os.path.join(album_dir, file)
        if not os.path.exists(dest_path):
            os.rename(FILE_PATH, dest_path)
            print(f"Moved: {file} -> {artist}/{album}/")
        else:
            print(f"File already exists in {artist}/{album}, skipping: {file}")