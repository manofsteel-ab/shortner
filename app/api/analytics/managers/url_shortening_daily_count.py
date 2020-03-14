from app.api.analytics.models.url_shortening_daily_count import UrlShorteningDailyCount
from app.api.imports import Managers


class UrlShorteningDailyCountManager:

    def __init__(self):
        self.Managers = Managers()
        self.model = UrlShorteningDailyCount
