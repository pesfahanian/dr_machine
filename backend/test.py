from inferences.core.model import Model

path = 'backend/media/2021-05-24_ava_lazemzadeh/covid_ct/cases/0a79338b-935e-42e1-ba6c-d6d83f2a1e5a/'

model = Model()
report = model.run_segmentation(directory_path=path)

print('-------', report)
