from celery import shared_task
from celery.result import AsyncResult

from backend.celery import app

from CT_LIS.core.model import CTLungInfectionSegmentationModel


@app.task(name='CT_LIS.execute_run_mode')
# @shared_task(name='CT_LIS.execute_run_mode')
def execute_run_model(case_directory_path, result_directory_path):
    print('-------- in get_results')
    model = CTLungInfectionSegmentationModel()
    model.run(case_directory_path=case_directory_path,
              result_directory_path=result_directory_path)


def get_results(id: str):
    print('-------- in get_results')
    r = AsyncResult(id, app=app)
    result = r.get()
    print(f'------- type result: {type(result)}')
    return result
