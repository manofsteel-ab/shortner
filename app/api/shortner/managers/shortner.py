from datetime import datetime

from app.api.imports import Managers
from app.api.shortner.models.shortner import Shortner
from app.commons.utils.constants import Error
from app.commons.utils.encoder import string_encode
from flask import current_app


class ShortnerManager:

    def __init__(self):
        self.Managers = Managers()
        self.model = Shortner

    def create_url_mapping(self, long_url, hash_val):
        instance = self.model.add(
            long_url=long_url,
            url_hash=hash_val,
            expires_at=datetime.utcnow(),
            commit=True
        )
        return instance

    def get_short_url(self, long_url, custom_code=""):
        if custom_code and self.model.fetch_by_hash(custom_code).first():
            raise Exception(Error.INVALID_CUSTOM_CODE)
        if custom_code:
            hash_val = custom_code
        else:
            hash_val = self.get_uniquer_hash()
        self.create_url_mapping(long_url, hash_val)
        return current_app.config['SHORT_URL'].format(hash_val)

    def get_uniquer_hash(self):
        seed = self.Managers.zoo_keeper().get_seed_val()
        return string_encode(str(seed))

    def get_original_url(self, hash_val=""):
        mapping = self.model.fetch_by_hash(hash_val).first()
        if mapping:
            mapping.update(hit_count=mapping.hit_count+1, commit=True)
            return mapping.long_url
        return None
