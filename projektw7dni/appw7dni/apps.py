from django.apps import AppConfig


class Appw7DniConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appw7dni'

    def ready(self):
        import appw7dni.signals
