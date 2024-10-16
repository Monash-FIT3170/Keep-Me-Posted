#!/bin/bash

# This script is used to start the frontend and backend servers
# Instructions:
# 1. Open terminal
# 2. cd to the root project directory "KEEP-ME-POSTED"
# 3. Run the script using the command "bash run_servers.sh"

# Get the directory of the script
DIR="$(cd "$(dirname "$0")" && pwd)"

# Function to start frontend server
echo "Starting frontend server..."
osascript -e 'tell application "Terminal" to do script "cd '$DIR'/frontend && npm run dev"'

# Function to start backend server
echo "Starting backend server..."
osascript -e 'tell application "Terminal" to do script "cd '$DIR'/backend && [ ! -d venv ] && python3 -m venv venv; source venv/bin/activate && cd kmp_backend && python manage.py makemigrations meetings && python manage.py migrate && python manage.py runserver"'
