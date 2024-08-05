import hashlib
from classes.user import User


class AuthenticationService:
    """
    Сервис для управления регистрацией и аутентификацией пользователей.
    """

    def __init__(self):
        self.current_user = None

    def register(self, user_class, username, email, password, *args):
        if any(user.username == username for user in User.users):
            return "Ошибка: Имя пользователя уже существует."

        user = user_class(username, email, password, *args)
        return f"Пользователь {username} зарегистрирован успешно."

    def login(self, username, password):
        for user in User.users:
            if user.username == username and user.check_password(user.password, password):
                self.current_user = user
                return f"Пользователь {username} вошел в систему."

        return "Ошибка: Неправильное имя пользователя или пароль."

    def logout(self):
        if self.current_user:
            username = self.current_user.username
            self.current_user = None
            return f"Пользователь {username} вышел из системы."
        return "Ошибка: В систему никто не вошёл."

    def get_current_user(self):
        if self.current_user:
            return self.current_user.get_details()
        return "Ошибка: В систему никто не вошёл."
