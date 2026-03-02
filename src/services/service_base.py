from src.configs.db import get_session


class ServiceBase:
    def __init__(self):
        with get_session() as session:
            self.session = session
        