#!/usr/bin/env bash
# Install Nginx and configure it

apt-get -y update
apt-get -y install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<!DOCTYPE html>
<html>
        <head>
        </head>
        <body>
                Holberton School
        </body>
</html>" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/server_name _;/a location /hbnb_static/ {\\n\\talias /data/web_static/current/;\\n\\t}\\n" /etc/nginx/sites-available/default
service nginx restart
exit 0
