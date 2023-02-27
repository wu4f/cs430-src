model_backend = 'sqlite3'
# model_backend = 'postgres'
# model_backend = 'pylist'

if model_backend == 'sqlite3':
    from gbmodel.model_sqlite3 import ModelSqlite as model
elif model_backend == 'pylist':
    from gbmodel.model_pylist import ModelPylist as model
elif model_backend == 'postgres':
    from gbmodel.model_sql_postgres import ModelSqlPostgres as model
else:
    raise ValueError("No appropriate databackend configured. ")

appmodel = model()

def get_model():
    return appmodel
