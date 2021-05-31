from django.apps import AppConfig


class InferencesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inferences'

    def ready(self):
        from inferences import signals
