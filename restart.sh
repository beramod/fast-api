source /home/centos/web-service/nines_api/nines_api.profile
sudo systemctl restart nginx.service
sudo systemctl restart gunicorn-nines-api.service