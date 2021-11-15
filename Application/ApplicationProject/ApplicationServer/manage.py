#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# Used this tutorial to setup: https://www.youtube.com/watch?v=zcALUNZNBUk
# https://www.bootstrapcdn.com/
# https://getbootstrap.com/docs/4.0/components/buttons/
# https://getbootstrap.com/docs/4.0/layout/grid/
# https://www.w3schools.com/html/html_links.asp
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ApplicationServer.settings')
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
