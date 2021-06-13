from backend.celery import app

from inferences.core.model import Model


@app.task(name='inferences.execute_run_inference')
def execute_run_inference(file_path: str):
    model = Model()
    report = model.run_inference(file_path=file_path)
    return report
