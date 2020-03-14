from datetime import datetime

from app.api.analytics.models.url_shortening_daily_count import UrlShorteningDailyCount
from app.api.imports import Managers
from app.commons.utils.constants import DateFormat


class UrlShorteningDailyCountManager:

    def __init__(self):
        self.manager = Managers()  # import class instance of manager
        self.model = UrlShorteningDailyCount  # model associated with current manager

    def log_shortening_count(self, success_count=0, failed_count=0):
        """
        Create/update url shortening success and failure count for current date
        """
        curr_date = datetime.utcnow().strftime(DateFormat.DEFAULT)
        current_count = self.model.fetch_by_date(curr_date).first()
        if current_count:
            current_count.update(
                success_count=current_count.success_count + success_count,
                failed_count=current_count.failed_count + failed_count,
                commit=True
            )
        else:
            self.model.add(
                date=curr_date,
                success_count=success_count,
                failed_count=failed_count,
                commit=True
            )
        return current_count
