#!/usr/bin/env bash

set -e  # Stop the script if any command fails

echo "Creating a virtual environment..."

# Create a virtual environment in the current directory
uv venv --seed

echo "Activating the virtual environment and upgrading pip..."
source .venv/Scripts/activate
uv pip install --upgrade pip

# Check if requirements.txt exists and install dependencies
if [ -f requirements.txt ]; then
    echo "Installing dependencies from requirements..."
    uv pip install -r requirements.txt
else
    echo "No requirements.txt file found. Skipping dependency installation."
fi

echo "Setup complete! The virtual environment is ready to use."