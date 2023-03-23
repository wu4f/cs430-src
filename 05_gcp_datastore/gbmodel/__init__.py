#model_backend = 'pylist'
#model_backend = 'datastore'
model_backend = 'firestore'

if model_backend == 'pylist':
    from .model_pylist import ModelPylist as model
elif model_backend == 'datastore':
    from .model_datastore import ModelDatastore as model
elif model_backend == 'firestore':
    from .model_firestore import ModelFirestore as model
else:
    raise ValueError("No appropriate databackend configured. ")

appmodel = model()

def get_model():
    return appmodel
