print("Starting app.py import...")
from flask import Flask
app = Flask(__name__)
print("Flask app created successfully.")
# ... rest of your code
if __name__ == '__main__':
    app.run()