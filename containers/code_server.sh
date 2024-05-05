#!/bin/bash

echo "Configuring Code Server container..."

echo "Set your root password:"
read -s rootPassword  # The '-s' flag hides input for privacy.
echo "Set your user password:"
read -s userPassword  # The '-s' flag hides input for privacy.

# Storing the Docker command in a variable.
run_cmd="docker run -d \
  --name=code-server \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/Vienna \
  -e PASSWORD=$userPassword \
  -e SUDO_PASSWORD=$rootPassword \
  -p 5500:8443 \
  -v //docker/appdata/code-server:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/code-server:latest"

# Printing the command as a string.
echo "$run_cmd"
