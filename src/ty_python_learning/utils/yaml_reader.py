import os

import yaml

from src.ty_python_learning.utils.typings import Any


class YamlReader(object):
    def __init__(self, yaml_filepath):
        if not os.path.exists(yaml_filepath):
            raise FileNotFoundError('File is not found: %s' % yaml_filepath)

        self.__yaml_filepath = yaml_filepath
        with open(self.__yaml_filepath) as file:
            self.__data = list(yaml.safe_load_all(file))

    @property
    def data(self) -> list[dict[str, Any]]:
        return self.__data

    def get(self, element, default=None, index=0) -> Any:
        return self.data[index].get(element, default)


PROJECT_PATH = r'S:\github\ty_python_learning'
LOGS_PATH = os.path.join(PROJECT_PATH, 'logs')
CONFIG_PATH = os.path.join(PROJECT_PATH, 'configs')

CONFIG = YamlReader(os.path.join(CONFIG_PATH, 'env.yaml'))
