from app.api.imports import Managers
from app.api.users import User


class UserManager:

    def __init__(self):
        self.manager = Managers()  # import class instance of manager
        self.model = User  # model associated with current manager

    def register_user(self):
        return 
