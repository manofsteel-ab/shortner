from app.api.imports import Managers
from app.api.users import User
from app.commons.utils.constants import UserType


class UserManager:

    def __init__(self):
        self.manager = Managers()  # import class instance of manager
        self.model = User  # model associated with current manager

    def register_user(self, user_attributes, commit=False):
        """
        user_attributes: RegisterUserSchema
        """
        user = self.model.add(data=user_attributes, commit=True)
        if user_attributes.get('user_roles'):
            for role in user_attributes.get('user_roles'):
                self.manager.user_role_manager().create_user_role(
                    user_id=user.id, role=role, commit=True
                )
        return user

    def log_me_in(self, username, password):
        users = self.model.fetch_by_username(username=username).all()
        if len(users) == 0:
            raise Exception("Invalid username")
        if len(users) > 1:
            raise Exception("Duplicate entry")
        if users[-1].check_password(password):
            return users[-1]
        else:
            raise Exception("Invalid password")

    def fetch_user(self, user_id):
        return self.model.fetch_by_user_id(user_id=user_id).first()

    def fetch_user_default_page(self, user_id):
        roles = self.manager.user_role_manager().fetch_roles(user_id=user_id)
        roles = [val.role_id for val in roles]
        if UserType.SYSTEM in roles:
            return "analytics.report"
        if UserType.NON_SYSTEM in roles:
            return "shortner.index"
