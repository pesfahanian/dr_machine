import os
import zipfile


def process_zipfile_case(zipfile_path, extract_path) -> None:
    print('-------- in process_zipfile_case')
    print(f'------- type zipfile_path: {type(zipfile_path)}')
    print(f'------- type extract_path: {type(extract_path)}')
    with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    os.remove(zipfile_path)
