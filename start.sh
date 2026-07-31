#!/bin/bash
# Start the web server in the background
gunicorn app:app --bind 0.0.0.0:$PORT &
# Start the bot
python3 main.py
