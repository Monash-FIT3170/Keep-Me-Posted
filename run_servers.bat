@echo off

:: Function to start frontend server
echo Starting frontend server...
start cmd /k "cd frontend && npm install && npm run dev"

:: Function to start backend server
echo Starting backend server...
start cmd /k "cd backend && (if not exist venv (python -m venv venv)) && (call venv\Scripts\activate.bat) && pip install -r requirements.txt && cd kmp_backend && python manage.py makemigrations meetings && python manage.py migrate && python manage.py runserver"
