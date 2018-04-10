# Modify username from llawrens to your own username on Google Cloud
# Modify bitbucket login to your own bitbucket username
# Modify servername in nginx/sites-available/itscs201 to match your hostname
# then do the restart

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y build-essential python-dev python-pip nginx-core nginx uwsgi uwsgi-plugin-python3
sudo pip install virtualenv
cd /var/www/html;
sudo chown -R llawrens .
git clone https://llawrens@bitbucket.org/llawrens/itscs201.git
cd /var/www/html/itscs201/
sudo mv etc/nginx/sites-available/itscs201 /etc/nginx/sites-available/itscs201
sudo mv etc/nginx/sites-enabled/itscs201 /etc/nginx/sites-enabled/itscs201
sudo vim /etc/nginx/sites-available/itscs201
sudo mv etc/uwsgi/apps-available/itscs201.ini /etc/uwsgi/apps-available/itscs201.ini
sudo mv etc/uwsgi/apps-enabled/itscs201.ini /etc/uwsgi/apps-enabled/itscs201.ini
cd /var/www/html/itscs201/www;
sudo mkdir env
sudo virtualenv -p python3 env
sudo chown -R llawrens env
sudo chgrp -R llawrens env
(/bin/bash -c "source env/bin/activate; pip3 install flask lockfile")
touch /tmp/itscs201.sock
sudo chown -R www-data /tmp/itscs201.sock /var/www/html
sudo chgrp -R www-data /tmp/itscs201.sock /var/www/html
sudo service nginx restart
sudo service uwsgi restart

# Certbot instructions
# These are untested instructions that will update nginx with the
#   certficate needed to do https.  It will automatically generate
#   the certs and update the nginx configuration file.
# 
# sudo add-apt-repository ppa:certbot/certbot -y
# sudo apt-get update
# sudo apt-get install certbot python-certbot-nginx -y
# sudo certbot --nginx 
#    ...Follow instructions
