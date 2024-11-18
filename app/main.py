from flask import Flask

# Flask application instance
app = Flask(__name__)

@app.route('/')
def hello():
    return "Thank You for the opportunity"

# Function to generate the HTML page for the game


