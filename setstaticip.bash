#!/bin/bash

# Retrieve current IP address
current_ip=$(hostname -I | awk '{print $1}')

# Check if an IP address is obtained
if [ -z "$current_ip" ]; then
    echo "Failed to retrieve current IP address."
    exit 1
fi

# Configure static IP address
cat <<EOF | sudo tee /etc/dhcpcd.conf > /dev/null
interface eth0
static ip_address=$current_ip/24
static routers=$(ip route show default | awk '/default/ {print $3}')
static domain_name_servers=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}')
EOF

# Restart dhcpcd service
sudo service dhcpcd restart

echo "Static IP address set to: $current_ip"
