from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):  # part 8
        import users.signals
