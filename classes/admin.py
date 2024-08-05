from classes.user import User

class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """
    def __init__(self, username, email, password, admin_level):
        super().__init__(username, email, password)
        self.admin_level = admin_level

    @staticmethod
    def list_users():
        return [user.get_details() for user in User.users]

    @staticmethod
    def delete_user(username):
        User.users = [user for user in User.users if user.username != username]

    def get_details(self):
        return f"Администратор: {self.username}, Уровень: {self.admin_level}"
