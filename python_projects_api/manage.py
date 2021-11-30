#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python_projects_api.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        print(
            "\nCouldn't import Django. \n\n1. Is it installed and "
            "available to the PYTHONPATH environment variable? \n2. Did you "
            "activate a virtual environment?\n\n"
        )
        raise exc
    execute_from_command_line(sys.argv)
