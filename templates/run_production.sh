# run_production.sh - Production run script
#!/bin/bash
export FLASK_APP=app.py
export DATABASE_URL=postgresql://user:pass@host/db  # Set your DB
gunicorn -w 4 -b 0.0.0.0:8000 app:app