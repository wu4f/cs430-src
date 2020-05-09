model_backend = 'dynamodb'
#model_backend = 'pylist'

if model_backend == 'dynamodb':
    from .model_dynamodb import model
elif model_backend == 'pylist':
    from .model_pylist import model
else:
    raise ValueError("No appropriate databackend configured. ")

appmodel = model()

def get_model():
    return appmodel
