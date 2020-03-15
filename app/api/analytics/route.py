from flask import Blueprint, render_template

from app.api.analytics.managers.url_shortening_daily_count import UrlShorteningDailyCountManager
from app.settings.custom_response import DefaultResponse
analyticBp = Blueprint('analytics', __name__, url_prefix='/api/analytics/')


@analyticBp.route('health/', methods=['GET'])
def app_health():
    return DefaultResponse(data={})


@analyticBp.route('', methods=['GET'])
def report():
    counts = UrlShorteningDailyCountManager().get_shorten_count_result()
    labels = counts.get('labels', [])
    success_counts = counts.get('success_counts', [])
    failed_count = counts.get('failed_counts', [])
    success_max = 100
    failed_max = 100
    if success_counts:
        success_max += max(success_counts)
    if failed_count:
        failed_max += max(failed_count)
    return render_template(
        'stats.html',
        title='Shortening Count(Daily basis)',
        success_max=success_max, failed_max=failed_max, labels=labels,
        success=success_counts,
        failed=failed_count,
    )
