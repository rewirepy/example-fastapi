
# example-fastapi

## A Simple Example of Using `rewire` with FastAPI

This repository showcases how to use `rewire` to set up a development environment for a FastAPI application.

### Configuration

Our application uses two configuration files: `config.yaml` and `.plugin.yaml`.

#### config.yaml - Application-Wide Configuration

This file contains settings that apply to the entire application, such as database URLs or third-party API keys.

#### .plugin.yaml - A List of Folders to be Automatically Loaded

By listing folders in this file, we can use `rewire` to automatically import files inside.

### Setup Instructions

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Start the application:
   ```
   python __main__.py
   ```
