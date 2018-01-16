#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
<<<<<<< HEAD
    execute_from_command_line(sys.argv)
=======
    execute_from_command_line(sys.argv)
>>>>>>> 8fef4b0bb4bd2930c78ef7f0ddcc5b1b878ee835
