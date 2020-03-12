from datetime import datetime

from app.api.manager_imports import Managers
from app.api.shortner.models.url import Url
from app.commons.utils.encoder import string_encode


class UrlManager:

    def __init__(self):
        self.Managers = Managers()

    def create_url_mapping(self, long_url, hash_val):
        Url.add(
            longUrl=long_url,
            urlHash=hash_val,
            expiresAt=datetime.utcnow(),
            commit=True
        )
        return self

    def get_short_url(self, long_url):
        hash_val = self.get_uniquer_hash()
        self.create_url_mapping(long_url, hash_val)
        return hash_val

    def get_uniquer_hash(self):
        seed = self.Managers.zoo_keeper().get_seed_val()
        return string_encode(str(seed))
