#!/usr/bin/env bash
# Exit on error
set -o errexit

# Change to the kmp_backend directory
cd kmp_backend

# Install dependencies
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
