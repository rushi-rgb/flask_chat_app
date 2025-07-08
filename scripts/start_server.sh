#!/bin/bash

cd /home/ubuntu/app

# Create virtualenv if it does not exist
if [ ! -d venv ]; then
  python3 -m venv venv
fi

# Activate virtualenv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Stop app in pm2 if running (ignore errors)
pm2 stop flask-realtime || true

# Start app with pm2 using python inside virtualenv
pm2 start venv/bin/python --name flask-realtime -- app.py

