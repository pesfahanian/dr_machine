import logging

from backend.celery import app

from CT_LIS.core.model import CTLungInfectionSegmentationModel
from CT_LIS.models import CTLungInfectionSegmentation

logger = logging.getLogger('backend')


@app.task(name='CT_LIS.execute_run_mode')
def execute_run_model(case_directory_path: str, result_directory_path: str,
                      id) -> None:
    print(type(id))
    logger.info('Executing run model...')

    model = CTLungInfectionSegmentationModel()

    logger.info('Model extracting features...')
    features = model.run(case_directory_path=case_directory_path,
                         result_directory_path=result_directory_path)
    logger.info('Model feature extraction completed!')
    logger.info(f'Extracted features are {features}.')

    logger.info('Proceding to save the extraced features...')
    try:
        instance = CTLungInfectionSegmentation.objects.get(id=id)
        instance.upper_left = features[0]
        instance.upper_right = features[2]
        instance.lower_left = features[1]
        instance.lower_middle = features[3]
        instance.lower_right = features[4]
        instance.save()
        logger.info('Extraced features saved!')
    except Exception as e:
        message = (f'Failed to save extracted features. Reason: {str(e)}.')
        logger.error(message)

    logger.info('Executing run model finished!')
