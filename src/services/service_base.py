from src.configs.db import Sessionmaker


class ServiceBase:
    def __init__(self):
        self.session = Sessionmaker()
        