from django.core.management.base import BaseCommand
from control import monitor
from threading import Thread

class Command(BaseCommand):
    help = 'Starts actuators control'

    def handle(self, *args, **kwargs):
        monitor.setup_mqtt()
        Thread(target = monitor.start_cron_warning()).start()
        Thread(target = monitor.start_cron_alert()).start()
        
        
       
