#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


'''
To delete the recent actions from the admin
1)In the root directory of the project, from terminal
2)Run the server python file from shell (python server.py shell) and then the following commands
------------------------------------------------
from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()
'''

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yesbroker.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
