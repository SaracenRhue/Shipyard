#!/bin/bash

if [ -n "$BASH_VERSION" ]; then
    echo "alias sy='curl -fsSL https://raw.githubusercontent.com/SaracenRhue/Shipyard/main/sy | bash -s'" >> ~/.bashrc
elif [ -n "$ZSH_VERSION" ]; then
    echo "alias sy='curl -fsSL https://raw.githubusercontent.com/SaracenRhue/Shipyard/main/sy | bash -s'" >> ~/.zshrc
fi