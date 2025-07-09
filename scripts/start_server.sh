#!/bin/bash

cd /home/ubuntu/app

# Create virtualenv if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt

# Restart application with PM2
pm2 delete flask-realtime || true
pm2 start venv/bin/python --name flask-realtime -- app.py

