#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# https://www.geeksforgeeks.org/rendering-data-frame-to-html-template-in-table-view-using-django-framework/
# https://stackoverflow.com/questions/56863105/how-do-i-pass-table-data-from-a-template-over-to-django-on-a-button-submit-click
# https://www.youtube.com/watch?v=zcALUNZNBUk
# https://www.kaggle.com/karthickveerakumar/startup-logistic-regression
# https://stackoverflow.com/questions/35659178/prevent-typing-in-text-field-input-even-though-field-is-not-disabled-read-only
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TutorialModel.settings')
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
