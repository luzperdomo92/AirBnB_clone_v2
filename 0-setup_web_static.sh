#!/usr/bin/env bash
# configure the web servers for deployment

# update and install Nginx
apt-get -y update
apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# Create the folders
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# fake html file with simple content
touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html

# Symbolic link
ln -sfn /data/web_static/releases/test/ /data/web_static/current

# give ownership persissions to ubuntu
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
sed -i "/server_name _;/a location /hbnb_static { alias /data/web_static/current/; autoindex off; }" /etc/nginx/sites-available/default

service nginx restart
