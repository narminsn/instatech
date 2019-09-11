from django.apps import AppConfig


class TheshotsConfig(AppConfig):
    name = 'theShots'

    def ready(self):
        import theShots.signals
