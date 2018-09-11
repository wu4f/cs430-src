model_backend = 'pylist'

def get_model():
    if model_backend == 'pylist':
        from .model_pylist import model
    else:
        raise ValueError("No appropriate databackend configured. ")
    return model()
