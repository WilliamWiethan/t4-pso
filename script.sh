sleep 10
python manage.py migrate
gunicorn --timeout 120 core.wsgi -b 0.0.0.0:8000

