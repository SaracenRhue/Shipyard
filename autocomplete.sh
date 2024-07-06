#!/bin/bash

#!/bin/bash

# Shipyard (sy) auto-completion script

_sy_completions() {
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="i install list search update remove log console stats backup clean rollback create-template analyze help"

    case "${prev}" in
        sy)
            COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
            return 0
            ;;
        install|i)
            # Fetch available container configs from the repository
            local containers=$(curl -s https://api.github.com/repos/SaracenRhue/Shipyard/contents/containers | grep '"name"' | sed -E 's/.*"name": "(.*)\.conf".*/\1/')
            COMPREPLY=( $(compgen -W "${containers}" -- ${cur}) )
            return 0
            ;;
        update|remove|log|console|stats|rollback)
            # For these commands, use running containers
            local containers=$(docker ps --format '{{.Names}}')
            COMPREPLY=( $(compgen -W "${containers}" -- ${cur}) )
            return 0
            ;;
        search)
            return 0
            ;;
        *)
            ;;
    esac

    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    return 0
}

# Register the completion function
complete -F _sy_completions sy

# Setup for various shells
if [ -n "$BASH_VERSION" ]; then
    if [ -f /etc/bash_completion ] && ! shopt -oq posix; then
        . /etc/bash_completion
    fi
elif [ -n "$ZSH_VERSION" ]; then
    autoload -U +X compinit && compinit
    autoload -U +X bashcompinit && bashcompinit
fi

# No need to modify .bashrc or .zshrc as this script is loaded every time sy is run