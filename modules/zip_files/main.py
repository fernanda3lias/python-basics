# ZIP - Compressing/Decompressing files with zipfile.ZipFile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Path
ROOT_PATH = Path(__file__).parent
ZIP_DIR_PATH = ROOT_PATH / 'zip_dir'
COMPRESSED_PATH = ZIP_DIR_PATH / 'compressed.zip'
UNCOMPRESSED_PATH = ROOT_PATH / 'uncomp_dir'

def create_files(qty: int, zip_dir: Path):
    for i in range(qty):
        text = 'file_%s' % i
        with open(zip_dir / f'{text}.txt', 'w') as file:
            file.write(text)

create_files(10, ZIP_DIR_PATH)

# Creating ZIP and adding files
with ZipFile(COMPRESSED_PATH, 'w') as zip:
    for root, dirs, files in os.walk(ZIP_DIR_PATH):
        for file in files:
            #print(file)
            zip.write(os.path.join(root, file), file)

# Reading files from ZIP
with ZipFile(COMPRESSED_PATH, 'r') as zip:
    for file in zip.namelist():
        print(file)

# Extracting files from ZIP
with ZipFile(COMPRESSED_PATH, 'r') as zip:
    zip.extractall(UNCOMPRESSED_PATH)