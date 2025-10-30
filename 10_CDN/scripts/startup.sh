#!/usr/bin/env bash
set -euxo pipefail

# Base tools (from DM template)
apt-get -y update
DEBIAN_FRONTEND=noninteractive apt-get -y install traceroute mtr tcpdump iperf whois host dnsutils siege

# Website provisioning (from your startup.sh)
apt-get install -y apache2 php wget
cd /var/www/html
rm -f index.html index.php
wget https://storage.googleapis.com/cs430/networking101/website/index.php
META_REGION_STRING=$(curl -s "http://metadata.google.internal/computeMetadata/v1/instance/zone" -H "Metadata-Flavor: Google")
REGION=$(echo "$META_REGION_STRING" | awk -F/ '{print $4}')
sed -i "s|region-here|$REGION|" index.php
systemctl enable apache2
systemctl restart apache2
