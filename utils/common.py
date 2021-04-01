import os
from typing import List, Dict


def get_os_envs(variables: List[str]) -> Dict[str, str]:
    if not variables:
        # todo: логирование
        raise ValueError('Got empty list of variable names')

    try:
        envs = {name: value for (name, value) in zip(variables, (os.environ[var] for var in variables))}
        # todo: логирование
    except KeyError as ex:
        # todo: логирование
        raise KeyError(f'Not found "{ex}" enviroment variable')
    except Exception as ex:
        # todo: логирование
        raise ex

    return envs



