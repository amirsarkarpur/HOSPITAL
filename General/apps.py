from django.apps import AppConfig


class GeneralConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'General'


    def ready(self):
        import General.signals