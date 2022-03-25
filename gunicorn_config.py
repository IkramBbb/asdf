command = '/Users/mac/Desktop/pythonProject/venv/bin/gunicorn'
pythonpath = '/Users/mac/Desktop/pythonProject/mysite'
bind = '127.0.0.1:8001'
workers = 3
user = 'mac'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=mysite.settings'