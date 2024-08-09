#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if bash is installed
if ! command_exists bash; then
    echo "Error: bash is not installed. Please install bash and try again."
    exit 1
fi

# Check if curl is installed
if ! command_exists curl; then
    echo "Error: curl is not installed. Please install curl and try again."
    exit 1
fi

# Check if docker is installed
if ! command_exists docker; then
    echo "Error: Docker is not installed. Please install Docker and try again."
    exit 1
fi

# Add alias to appropriate shell configuration file
if [ -n "$BASH_VERSION" ]; then
    echo "alias sy='bash <(curl -fsSL https://raw.githubusercontent.com/SaracenRhue/Shipyard/main/sy)'" >> ~/.bashrc
    source ~/.bashrc
elif [ -n "$ZSH_VERSION" ]; then
    echo "alias sy='bash <(curl -fsSL https://raw.githubusercontent.com/SaracenRhue/Shipyard/main/sy)'" >> ~/.zshrc
    source ~/.zshrc
else
    echo "Error: Unsupported shell. Please add the alias manually."
    exit 1
fi
