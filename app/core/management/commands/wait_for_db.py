"""
Django command to wait for db to be available
"""
from typing import Any, Optional
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """ Django command to wait for db"""
    
    def handle(self, *args: Any, **options):
        pass
