from src.configs.db import get_session


class ServiceBase:
    def __init__(self):
        self.session = get_session()
        