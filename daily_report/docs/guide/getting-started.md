# Getting Started with MkDocs

## Installation

To get started with MkDocs, you'll need Python installed on your system. Then you can install MkDocs using pip:

```bash
pip install mkdocs
pip install mkdocs-material
```

## Creating a New Project

1. Create a new project:
   ```bash
   mkdocs new my-project
   cd my-project
   ```

2. Start the development server:
   ```bash
   mkdocs serve
   ```

3. Open your browser and visit `http://127.0.0.1:8000`

## Project Layout

    mkdocs.yml    # The configuration file
    docs/
        index.md  # The documentation homepage
        ...       # Other markdown pages, images and other files

## Basic Commands

* `mkdocs serve` - Start the live-reloading docs server
* `mkdocs build` - Build the documentation site
* `mkdocs -h` - Print help message and exit

!!! tip "Pro Tip"
    Use `mkdocs serve` during development to preview your changes in real-time!
