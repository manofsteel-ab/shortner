"""
This file is to handle all manager related imports.
 Its very helpful to avoid circular dependency and we can track all managers list and import
"""


class Managers:

    def __init__(self):
        pass

    @property
    def zoo_keeper_manager(self):
        from app.api.zoo_keeper.managers.zoo_keeper import ZooKeeper
        return ZooKeeper

    @property
    def daily_counter_manager(self):
        from app.api.analytics.managers.url_shortening_daily_count import UrlShorteningDailyCountManager
        return UrlShorteningDailyCountManager
