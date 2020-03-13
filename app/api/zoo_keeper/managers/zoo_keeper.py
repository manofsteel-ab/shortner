from app.api.imports import Managers
from app.api.zoo_keeper.models.seed import Seed


class ZooKeeper:

    def __init__(self):
        self.Managers = Managers

    def get_seed_val(self):
        return Seed.get_next_seed()
