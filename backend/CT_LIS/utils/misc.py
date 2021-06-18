import os
import zipfile


def extract_zipfile_case(zipfile_path: str, extract_path: str) -> None:
    with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    os.remove(zipfile_path)


def validate_result_directory_existence(result_directory_path: str) -> None:
    if not os.path.isdir(result_directory_path):
        os.makedirs(result_directory_path)
