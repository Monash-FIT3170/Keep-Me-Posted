#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Print commands to the terminal
set -x

# Install Python dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Optionally: create a superuser (remove this if not needed)
# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell
