#model_backend = 'pydict'
#model_backend = 'sqlite3'
model_backend = 'sqlite3'

def get_model():
    if model_backend == 'sqlite3':
        from .model_sqlite3 import model
    elif model_backend == 'pydict':
        from .model_pydict import model
    else:
        raise ValueError("No appropriate databackend configured. ")
    return model()
