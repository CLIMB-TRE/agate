from django.apps import AppConfig
import sys


class AgateConfig(AppConfig):
    name = 'agate'

    def ready(self):
        """ Import our scheduled tasks module, which will register the tasks with the scheduler """
        if 'migrate' not in sys.argv:
            from . import scheduled_tasks
