import os

from django.db.models.signals import post_save
from django.dispatch import receiver

from CT_LIS.core.model import CTLungInfectionSegmentationModel
from CT_LIS.models import CTLungInfectionSegmentation
# from CT_LIS.tasks import execute_run_segmentation, get_results
from CT_LIS.utils.dicom_utils import read_metadata
from CT_LIS.utils.misc import process_zipfile_case


@receiver(post_save, sender=CTLungInfectionSegmentation)
def run_CTLungInfectionSegmentation(sender, instance, created, **kwargs):
    if created:
        print('Running CT lung infection segmentation....')
        # metadata = read_metadata(instance.file)
        # instance.patient_id = metadata['PatientID']
        # instance.patient_sex = metadata['PatientSex']
        # instance.patient_age = int(metadata['PatientAge'][:-1])
        # instance.save()

        # model = Model()
        # report = model.run_inference(file_path=instance.file.path)

        # report = execute_run_inference.delay(file_path=instance.file.path)

        case_directory_path = f'{instance.cases_directory_path}/{instance.id}/'

        process_zipfile_case(instance.file.path, case_directory_path)

        print(case_directory_path)

        result_directory_path = f'{instance.results_directory_path}/{instance.id}/'

        print(result_directory_path)

        if not os.path.isdir(result_directory_path):
            os.makedirs(result_directory_path)

        model = CTLungInfectionSegmentationModel()

        model.run(case_directory_path=case_directory_path,
                  result_directory_path=result_directory_path)

        # task = execute_run_segmentation.delay(directory_path=case_directory_path)
        # task_id = task.id
        # report = get_results(task_id)

        # model = Model()
        # report = model.run_segmentation(directory_path=extract_path)

        # print('-------', report)

        # report_save_path = f'{instance.results_directory_path}/{instance.id}.txt'
        # f = open(report_save_path, 'w')
        # f.write(str(report))
        # f.close()

        # instance.report = report
        # instance.save()
