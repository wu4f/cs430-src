#model_backend = 'pylist'
model_backend = 'dynamodb'

if model_backend == 'pylist':
    from .model_pylist import model
elif model_backend == 'dynamodb':
    from .model_dynamodb import model
else:
    raise ValueError("No appropriate databackend configured. ")

appmodel = model()

def get_model():
    return appmodel
