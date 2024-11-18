from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello():
    """Handles the root route and returns a greeting."""
    return render_template_string("<h1>Thank You for the opportunity</h1>")

if __name__ == '__main__':
    # Ensure the app runs on port 80 and binds to all available interfaces
    app.run(debug=True, host='0.0.0.0', port=80)
