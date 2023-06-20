model_backend = 'datastore'
#model_backend = 'firestore'

if model_backend == 'datastore':
    from .model_datastore import model
elif model_backend == 'firestore':
    from .model_firestore import model
else:
    raise ValueError("No appropriate databackend configured. ")

appmodel = model()

def get_model():
    return appmodel
