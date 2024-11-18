import os
import sys


def main() -> None:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taxi_service.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure you installed it and "
            "Make sure you're PYTHONPATH have correct variables."
            "Make sure you activate venv"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
