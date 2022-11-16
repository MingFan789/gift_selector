import yaml

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ConfigContext(metaclass=Singleton):
    def __init__(self) -> None:
        print("Init config first time")
        # read from yaml
        with open("./resource/config.yml", "r") as stream:
            self.config:dict = yaml.safe_load(stream)
