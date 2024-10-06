#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def check_env_vars():
    """Log missing environment variables"""
    required_env_vars = ['GEMINI_API_KEY', 'ASSEMBLYAI_API_KEY', 'SMTP_EMAIL', 'SMTP_API_KEY']
    for var in required_env_vars:
        env_var = os.getenv(var)
        if not env_var or env_var == "REPLACE_WITH_API_KEY":
            print(f"Missing required environment variable: {var}")


def main():
    """Run administrative tasks."""
    check_env_vars()  # check environment variables before running anything

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kmp_backend.settings')
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
