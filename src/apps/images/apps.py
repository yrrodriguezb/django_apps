from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = 'images'

    def ready(self):
        # import signal handlers
        import apps.images.signals