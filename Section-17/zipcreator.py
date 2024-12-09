import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "Compressed.Zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath) # This will remove the absolute path and make only the file name available
            archive.write(filepath, arcname=filepath.name) # The argument arcname = filepath.name will provide just the name of the file, exculding the path 


if __name__ == "__main__":
    make_archive (filepaths=["todos.txt", "function.py"], dest_dir="dest" )