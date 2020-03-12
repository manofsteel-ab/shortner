class Models:

    def __init__(self):
        pass

    @property
    def url(self):
        from app.api.shortner.models.url import Url
        return Url

    @property
    def seed(self):
        from app.api.zoo_keeper.models.seed import Seed
        return Seed
