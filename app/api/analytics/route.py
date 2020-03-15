from flask import Blueprint, render_template

from app.api.analytics.managers.url_shortening_daily_count import UrlShorteningDailyCountManager
from app.settings.custom_response import DefaultResponse
analyticBp = Blueprint('analytics', __name__, url_prefix='/api/analytics/')


@analyticBp.route('health/', methods=['GET'])
def app_health():
    return DefaultResponse(data={})


@analyticBp.route('/shorten_count/', methods=['GET'])
def shorten_count():
    counts = UrlShorteningDailyCountManager().get_shorten_count_result()
    labels = counts.get('labels', [])
    success_counts = counts.get('success_counts', [])
    failed_count = counts.get('failed_counts', [])
    y_limit = 1000
    if success_counts:
        y_limit += max(success_counts)
    return render_template(
        'stats.html',
        title='Shortening Count(Daily basis)',
        max=y_limit, labels=labels,
        values=success_counts
    )
