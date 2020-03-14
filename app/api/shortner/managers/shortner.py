from datetime import datetime

from app.api.imports import Managers
from app.api.shortner.models.shortner import Shortner
from app.commons.utils.constants import Error
from app.commons.utils.encoder import string_encode
from flask import current_app


class ShortnerManager:

    def __init__(self):
        self.manager = Managers()  # import class instance of manager
        self.model = Shortner  # model associated with current manager

    def create_url_mapping(self, long_url, hash_val):
        """
        Create entry in model
        """
        instance = self.model.add(
            long_url=long_url,
            url_hash=hash_val,
            expires_at=datetime.utcnow(),
            commit=True
        )
        return instance

    def get_short_url(self, long_url, custom_code=""):
        """
        generate random short code for given long url. if custom code is given, then  validate custom code.
        Also update analytic daily count manger about the success and failed result.
        return: shorted code if success otherwise raise Exception
        """
        if custom_code and self.model.fetch_by_hash(custom_code).first():
            self.manager.daily_counter_manager().log_shortening_count(failed_count=1)
            raise Exception(Error.INVALID_CUSTOM_CODE)
        if custom_code:
            hash_val = custom_code
        else:
            hash_val = self.get_uniquer_hash()
        self.create_url_mapping(long_url, hash_val)
        self.manager.daily_counter_manager().log_shortening_count(success_count=1)
        return current_app.config['SHORT_URL'].format(hash_val)

    def get_uniquer_hash(self):
        """
        Ask zoo keeper manager for hash code (zoo keeper will handle hash code generation logic)
        """
        seed = self.manager.zoo_keeper_manager().get_seed_val()
        return string_encode(str(seed))

    def get_original_url(self, hash_val=""):
        """
        Fetch original url using given hash value
        """
        mapping = self.model.fetch_by_hash(hash_val).first()
        if mapping:
            mapping.update(hit_count=mapping.hit_count+1, commit=True)
            return mapping.long_url
        return None
