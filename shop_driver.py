from classes.customer import Customer
from classes.admin import Admin
from classes.auth_service import AuthenticationService

# Создаем экземпляр сервиса аутентификации
auth_service = AuthenticationService()

# Регистрация пользователей
print("Регистрация пользователей:")
print(auth_service.register(Customer, "john_doe", "john@example.com", "password123", "Улица 1"))
print(auth_service.register(Admin, "admin_user", "admin@example.com", "adminpass", "super"))
print("")  # Пустая строка

# Аутентификация
print("Аутентификация пользователей:")
print(auth_service.login("john_doe", "password123"))  # Успешная аутентификация
print(auth_service.get_current_user())  # Получаем данные текущего пользователя
print(auth_service.logout())  # Выход из системы
print(auth_service.get_current_user())  # Проверяем, кто сейчас в системе

print("")  # Пустая строка

# Повторный вход
print("Повторный вход:")
print(auth_service.login("admin_user", "adminpass"))  # Успешная аутентификация администратора
print(auth_service.get_current_user())  # Получаем данные текущего администратора

# Административные функции
admin = Admin("admin_user", "admin@example.com", "adminpass", "super")
print("\nПользователи в системе перед удалением:")
print(admin.list_users())  # Список пользователей до удаления

# Удаляем пользователя
admin.delete_user("john_doe")
print("Пользователи в системе после удаления 'john_doe':")
print(admin.list_users())  # Список пользователей после удаления

