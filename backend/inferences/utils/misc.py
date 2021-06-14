import os
import zipfile


def process_zipfile_case(zipfile_path, extract_path):
    with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    os.remove(zipfile_path)
