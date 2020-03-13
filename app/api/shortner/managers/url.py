from datetime import datetime

from app.api.imports import Managers
from app.api.shortner.models.url import Url
from app.commons.utils.encoder import string_encode


class UrlManager:

    def __init__(self):
        self.Managers = Managers()
        self.model = Url

    def create_url_mapping(self, long_url, hash_val):
        instance = self.model.add(
            longUrl=long_url,
            urlHash=hash_val,
            expiresAt=datetime.utcnow(),
            commit=True
        )
        return instance

    def get_short_url(self, long_url, custom_code=""):
        if custom_code:
            hash_val = custom_code
        else:
            hash_val = self.get_uniquer_hash()
        if self.model.fetch_by_hash(custom_code).first():
            pass
        self.create_url_mapping(long_url, hash_val)
        return hash_val

    def get_uniquer_hash(self):
        seed = self.Managers.zoo_keeper().get_seed_val()
        return string_encode(str(seed))

    def get_original_url(self, hash_val=""):
        mapping = self.model.fetch_by_hash(hash_val).first()
        if mapping:
            mapping.update(hitCount=mapping.hitCount+1, commit=True)
            return mapping.longUrl
        return None
