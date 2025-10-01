from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback_secret_key_for_local_testing')

@app.route('/')
def landing():
    return render_template('landing.html')