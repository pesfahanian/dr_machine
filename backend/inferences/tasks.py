from celery.result import AsyncResult

from backend.celery import app

# from inferences.core._model import Model
from inferences.core.model import Model


# @app.task(name='inferences.execute_run_inference')
# def execute_run_inference(file_path: str):
#     model = Model()
#     report = model.run_inference(file_path=file_path)
#     return report


@app.task(name='inferences.execute_run_segmentation')
def execute_run_segmentation(directory_path):
    model = Model()
    report = model.run_segmentation(directory_path=directory_path)
    return report


def get_results(id: str):
    r = AsyncResult(id, app=app)
    result = r.get()
    return result
