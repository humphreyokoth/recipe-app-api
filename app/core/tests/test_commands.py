"""
Test cudtom Django management commands.
"""
from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test command"""
    def test_wait_for_db_ready(self):
        """Test waiting for db if db ready"""

