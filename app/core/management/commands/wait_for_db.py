"""
Django command to wait for db to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """ Django command to wait for db"""

    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write('Waiting for db to be available....')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error,OperationalError):
                self.stdout.write('Database Unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))