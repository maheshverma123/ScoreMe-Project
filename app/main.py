from flask import Flask, render_template_string
from flask_wtf.csrf import CSRFProtect

# Flask application instance
app = Flask(__name__)

# Enable CSRF protection
app.config['SECRET_KEY'] = 'VzUbeqxdRU3PMUmw4XYlkcym'  # Make sure to set a strong secret key
csrf = CSRFProtect(app)

@app.route('/')
def hello():
    """Handles the root route and returns a greeting."""
    return render_template_string("<h1>Thank You for the opportunity</h1>")

if __name__ == '__main__':
    # Ensure the app runs on port 80 and binds to all available interfaces
    app.run(debug=True, host='0.0.0.0', port=80)
