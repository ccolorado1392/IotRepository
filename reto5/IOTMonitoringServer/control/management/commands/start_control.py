from django.core.management.base import BaseCommand
from control import monitor


class Command(BaseCommand):
    help = 'Starts actuators control'

    def handle(self, *args, **kwargs):
        monitor.setup_mqtt()
        monitor.analyze_warning()
        monitor.start_cron_alert()
       
