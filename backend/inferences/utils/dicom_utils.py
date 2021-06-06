import pydicom as dcm

DATA_ELEMENTS = ['PatientID', 'PatientSex', 'PatientAge']


def read_metadata(file) -> dict:
    scan = dcm.dcmread(file)
    metadata = {}
    for D in DATA_ELEMENTS:
        metadata[D] = scan.data_element(D).value
    return metadata
