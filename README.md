# Shipyard (sy) - Container Management Tool

Shipyard is a powerful command-line tool designed to simplify Docker container management. It provides an easy-to-use interface for installing, updating, and managing containers based on pre-configured templates.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Commands](#commands)
4. [Creating Container Templates](#creating-container-templates)
5. [Contributing Templates](#contributing-templates)
6. [License](#license)

## Installation

You can easily install Shipyard using the following command:

```bash
curl -fsSL https://raw.githubusercontent.com/SaracenRhue/Shipyard/main/install.sh | bash
```

This will download and install Shipyard on your system.

## Usage

After installation, you can use Shipyard with the `sy` command. Here's the basic syntax:

```bash
sy [command] [options]
```

To see a list of available commands, run:

```bash
sy help
```

## Commands

- `install [--dry-run] <container-name>`: Install a new container
- `list`: List all available container templates
- `search <keyword>`: Search for container templates
- `update <container-name>`: Update a specific container
- `update -a|--all`: Update all containers
- `remove <container-name>`: Remove a specific container
- `log <container-name>`: Display logs of a container
- `console <container-name>`: Access a container's console
- `stats [container-name]`: Display resource usage statistics
- `rollback <container-name>`: Rollback a container to its previous version
- `clean`: Clean up Docker resources and appdata directories
- `backup`: Backup container data
- `create-template`: Create a new container template
- `analyze <repository> [tag]`: Analyze a Docker Hub image and generate a template

## Creating Container Templates

To create a new container template:

1. Run `sy create-template`
2. Enter the full Docker run command when prompted
3. Provide a name for the template
4. The tool will generate a `.conf` file with the template

Alternatively, you can use `sy analyze <repository> [tag]` to generate a template from a Docker Hub image.

## Contributing Templates

We welcome contributions of new container templates to Shipyard. If you have a template you'd like to share:

1. Create a new `.conf` file in the `containers` directory
2. Ensure your template follows the existing format
3. Submit a pull request with your new template

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, please file an issue on the [GitHub issue tracker](https://github.com/SaracenRhue/Shipyard/issues).

---

Shipyard - Simplifying Docker container management, one command at a time.