from django.apps import AppConfig
import os
import django


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        import home.signals

        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")

        os.system('python script.py')
