#!/usr/bin/env bash
# configure the web servers for deployment

# update and install Nginx
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# Create the folders
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# fake html file with simple content
sudo touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Symbolic link
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current

# give ownership persissions to ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
sudo sed -i "47i location /hbnb_static { alias /data/web_static/current/; autoindex off; }" /etc/nginx/sites-available/default

sudo service nginx restart
