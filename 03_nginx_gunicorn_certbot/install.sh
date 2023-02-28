#!/bin/bash
# Installs on Debian/Ubuntu VM
# Make sure script is called with DNS name desired
if [ $# -ne 2 ]; then
    echo "Usage: sudo install.sh <DNS_Name> <Email_Address>"
fi

# Name the service based on first part of DNS name
SITE=`echo $1 | sed -e 's/\..*//'`

# Install all required system packages
apt-get update
apt-get install -y nginx python3 python3-pip python3-venv nginx certbot python3-certbot-nginx

# Install all required python packages
python3 -m venv env
source env/bin/activate
pip3 install --upgrade -r requirements.txt

# Set up systemd service for site
sed s+PROJECT_USER+$SUDO_USER+ etc/systemd.template | sed s+PROJECT_DIR+$PWD+ > /etc/systemd/system/$SITE.service

# Configure nginx for site
sed s+PROJECT_HOST+$1+ etc/nginx.template | sed s+PROJECT_DIR+$PWD+ > /etc/nginx/sites-available/$SITE
ln -s /etc/nginx/sites-available/$SITE /etc/nginx/sites-enabled

# Restart all services
systemctl start $SITE
systemctl enable $SITE
systemctl restart nginx

certbot --nginx -d $1 --noninteractive -m $2 --agree-tos --redirect

echo "Installation complete."
