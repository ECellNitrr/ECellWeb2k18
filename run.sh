source envars.sh

sudo cp ecellnginx /etc/nginx/sites-available
sudo service nginx restart

gunicorn --bind 0.0.0.0:8000 server.wsgi:application --workers 3