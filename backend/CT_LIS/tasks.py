from celery.result import AsyncResult

from backend.celery import app

from CT_LIS.core.model import CTLungInfectionSegmentationModel


@app.task(name='CT_LIS.execute_run_mode')
def execute_run_model(case_directroy_path, result_directory_path):
    print('-------- in get_results')
    model = CTLungInfectionSegmentationModel()
    report = model.run(directory_path=case_directroy_path,
                       result_path=result_directory_path)
    print(f'------- type result: {type(report)}')
    return report


def get_results(id: str):
    print('-------- in get_results')
    r = AsyncResult(id, app=app)
    result = r.get()
    print(f'------- type result: {type(result)}')
    return result
