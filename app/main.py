import sys
import random
import os
from wsgiref.simple_server import make_server

# Function to generate the HTML page for the game
def generate_html():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Catch the Square Game</title>
        <style>
            body {
                text-align: center;
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
            }
            canvas {
                border: 1px solid black;
                background-color: white;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>

    <h1>Catch the Square Game</h1>
    <p id="score">Score: 0</p>
    <canvas id="gameCanvas" width="600" height="400"></canvas>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const squareSize = 50;
        let score = 0;
        let squareX = Math.random() * (canvas.width - squareSize);
        let squareY = Math.random() * (canvas.height - squareSize);

        // Function to update the score on the screen
        function updateScore() {
            document.getElementById('score').innerText = "Score: " + score;
        }

        // Function to move square to a random position
        function moveSquare() {
            squareX = Math.random() * (canvas.width - squareSize);
            squareY = Math.random() * (canvas.height - squareSize);
        }

        // Game loop to render the game
        function gameLoop() {
            ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
            ctx.fillStyle = 'red';
            ctx.fillRect(squareX, squareY, squareSize, squareSize); // Draw the square

            updateScore(); // Update the score on the page
        }

        // Mouse click handler
        canvas.addEventListener('click', (event) => {
            const mouseX = event.offsetX;
            const mouseY = event.offsetY;

            // Check if the square is clicked
            if (mouseX >= squareX && mouseX <= squareX + squareSize &&
                mouseY >= squareY && mouseY <= squareY + squareSize) {
                score++;  // Increment score
                moveSquare();  // Move square to a new random position
            }
        });

        // Run the game loop at 30 FPS
        setInterval(gameLoop, 1000 / 30);
    </script>

    </body>
    </html>
    """
# WSGI application
def application(environ, start_response):
    # Serve the HTML content
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [generate_html().encode('utf-8')]

# Run the server (for testing purpose, this is not used in production with Apache)
if __name__ == '__main__':
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()
