"""
This file is to handle all manager related imports.
 Its very helpful to avoid circular dependency and we can track all managers list and import
"""


class Managers:

    def __init__(self):
        pass

    @property
    def url(self):
        from app.api.shortner.managers.shortner import ShortnerManager
        return ShortnerManager

    @property
    def zoo_keeper(self):
        from app.api.zoo_keeper.managers.zoo_keeper import ZooKeeper
        return ZooKeeper
