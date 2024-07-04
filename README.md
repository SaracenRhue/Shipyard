Certainly! Here's a comprehensive README for the Shipyard project:

---

# Shipyard

A package manager for containers

## Overview

Shipyard (sy) is a container management tool that simplifies the installation, listing, updating, and removal of Docker containers. It allows you to manage your Docker containers with easy-to-use commands.

## Features

- **Install**: Install new containers based on predefined configurations.
- **List**: List all installed containers with their current status.
- **Update**: Update specified containers or all containers to the latest image.
- **Remove**: Remove specified containers.

## Installation

You can easily install Shipyard using the following command:

```bash
curl -fsSL https://raw.githubusercontent.com/SaracenRhue/Shipyard/main/install.sh | bash
```

This will download and install Shipyard on your system.

## Usage

After installation, you can use Shipyard with the `sy` command followed by various subcommands.

### Commands

#### Install a New Container

```bash
sy install <container-name>
```
or
```bash
sy i <container-name>
```

This command installs a new container based on the configuration available at `https://raw.githubusercontent.com/SaracenRhue/Shipyard/main/containers/<container-name>.conf`.

#### List All Installed Containers

```bash
sy list
```

This command lists all installed containers with their names, images, and statuses.

#### Update a Specified Container

```bash
sy update <container-name>
```

This command updates the specified container to the latest image.

#### Update All Containers

```bash
sy update -a
```
or
```bash
sy update --all
```

This command updates all installed containers to their latest images.

#### Remove a Specified Container

```bash
sy remove <container-name>
```

This command removes the specified container.

#### Show Help

```bash
sy help
```

This command displays the help menu with usage information for all commands.

## Usage Without Installation

If you prefer to use Shipyard without installing it, you can run it directly from the source:

```bash
curl -fsSL https://raw.githubusercontent.com/SaracenRhue/Shipyard/main/sy | bash -s
```

This will download and execute the latest version of Shipyard.

## Example

```bash
# Install a container
sy install my-container

# List all containers
sy list

# Update a specific container
sy update my-container

# Update all containers
sy update --all

# Remove a container
sy remove my-container
```

## Configuration

Shipyard uses configuration files for each container, which are hosted at `https://raw.githubusercontent.com/SaracenRhue/Shipyard/main/containers/`. Each configuration file defines the necessary Docker run command and other parameters required to set up the container.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request on the [GitHub repository](https://github.com/SaracenRhue/Shipyard). Feel free to add container templates for other containers you use!
