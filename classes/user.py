import hashlib  # Добавлен импорт hashlib

class User:
    """
    Базовый класс, представляющий пользователя.
    """
    users = []  # Список для хранения всех пользователей

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.hash_password(password)
        User.users.append(self)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def check_password(stored_password, provided_password):
        return stored_password == User.hash_password(provided_password)

    def get_details(self):
        return f"Пользователь: {self.username}, Email: {self.email}"
