from datetime import datetime

from app.api.analytics.models.url_shortening_daily_count import UrlShorteningDailyCount
from app.api.imports import Managers
from app.commons.utils.constants import DateFormat, UserType


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

    def get_shorten_count_result(self):
        all_count = self.model.custom_query().all()
        response = {
            'labels': [],
            'success_counts': [],
            'failed_counts': []
        }
        for count in all_count:
            dt_str = count.date.strftime(DateFormat.DEFAULT_FOR_LABEL)
            response['labels'].append(dt_str)
            response['success_counts'].append(count.success_count)
            response['failed_counts'].append(count.failed_count)
        return response

    def validate_access(self, user_id):
        roles = self.manager.user_role_manager().fetch_roles(user_id=user_id)
        roles = [val.role_id for val in roles]
        print(roles)
        if UserType.SYSTEM in roles:
            return True
        return False
