#!/bin/bash

echo "Configuring DuckDNS container..."

# Set defaults
default_token="YOUR_DUCKDNS_TOKEN"
default_container_name="duckdns"
default_timezone="Europe/Vienna"
default_subdomains="mydomain.duckdns.org"
default_log_policy="false"
default_volume_path="/appdata/duckdns"
default_restart_policy="unless-stopped"

# Prompt user for inputs with defaults
echo "DuckDNS token (default: $default_token):"
read -s token && token=${token:-$default_token}

echo "Container name (default: $default_container_name):"
read containerName && containerName=${containerName:-$default_container_name}

echo "Time zone (default: $default_timezone):"
read timezone && timezone=${timezone:-$default_timezone}

echo "Subdomains (default: $default_subdomains):"
read subdomains && subdomains=${subdomains:-$default_subdomains}

echo "Log file (default: $default_log_policy):"
read logPolicy && logPolicy=${logPolicy:-$default_log_policy}

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
-e SUBDOMAINS=$subdomains\
-e TOKEN=$token \
-e LOG_FILE=$logPolicy \
-v $volumePath:/config \
--restart $restartPolicy \
lscr.io/linuxserver/duckdns:latest"

# Printing the command as a string.
echo "$run_cmd"