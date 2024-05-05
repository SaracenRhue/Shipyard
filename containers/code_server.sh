#!/bin/bash

echo "Configuring Code Server container..."

# Set defaults
default_root_password="toor"
default_user_password="nodlehs"
default_container_name="code-server"
default_timezone="Europe/Vienna"
default_port="8443"
default_volume_path="/appdata/code-server"
default_restart_policy="unless-stopped"

# Prompt user for inputs with defaults
echo "Set your root password (default: $default_root_password):"
read -s rootPassword && rootPassword=${rootPassword:-$default_root_password}

echo "Set your user password (default: $default_user_password):"
read -s userPassword && userPassword=${userPassword:-$default_user_password}

echo "Container name (default: $default_container_name):"
read containerName && containerName=${containerName:-$default_container_name}

echo "Time zone (default: $default_timezone):"
read timezone && timezone=${timezone:-$default_timezone}

echo "Port (default: $default_port):"
read port && port=${port:-$default_port}

echo "/config path (default: $default_volume_path):"
read volumePath && volumePath=${volumePath:-$default_volume_path}

echo "Restart policy (default: $default_restart_policy):"
read restartPolicy && restartPolicy=${restartPolicy:-$default_restart_policy}

# Storing the Docker command in a variable.
run_cmd="docker run -d \
  --name=$containerName \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=$timezone \
  -e PASSWORD=$userPassword \
  -e SUDO_PASSWORD=$rootPassword \
  -p $port:8443 \
  -v $volumePath:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/code-server:latest"

# Printing the command as a string.
echo "$run_cmd"
