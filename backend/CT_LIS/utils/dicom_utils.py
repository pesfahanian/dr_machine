import pydicom as dcm

DATA_ELEMENTS = ['PatientID', 'PatientSex', 'PatientAge']


def read_metadata(file) -> dict:
    print('-------- in read_metadata')
    print(f'------- type file: {type(file)}')
    scan = dcm.dcmread(file)
    metadata = {}
    for D in DATA_ELEMENTS:
        metadata[D] = scan.data_element(D).value
    return metadata
