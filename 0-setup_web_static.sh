#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

sudo apt-get update
sudo apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Hello World!" > /var/www/html/index.html
echo "Ceci n'est pas une page" > /var/www/html/404.html
echo "Holberton School" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index index.html;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html;
    }

    location /redirect_me {
        return 301 https://github.com/Abdullrahmen;
    }

    error_page 404 /404.html;
    location /404 {
      internal;
    }
}" > /etc/nginx/sites-available/default

sudo service nginx restart
