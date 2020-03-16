from app.api.imports import Managers
from app.api.users.models import UserRole


class UserRoleManager:

    def __init__(self):
        self.manager = Managers()  # import class instance of manager
        self.model = UserRole  # model associated with current manager

    def create_user_role(self, user_id=None, role=None, commit=True):
        in_validation = [
            not user_id, not role
        ]
        if any(in_validation):
            raise Exception("Invalid request")
        user_role = self.model.add(
            user_id=user_id,
            role_id=role,
            commit=False
        )
        if commit:
            user_role.commit()
        return user_role

    def fetch_roles(self, user_id):
        return self.model.fetch_by_user_id(user_id).all()
