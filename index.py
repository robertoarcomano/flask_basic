from flask import Flask
from flask_basicauth import BasicAuth

# Create a Flask application
app = Flask(__name__)

# Configure basic authentication
app.config['BASIC_AUTH_USERNAME'] = 'username'
app.config['BASIC_AUTH_PASSWORD'] = 'password'
app.config['BASIC_AUTH_FORCE'] = True  # Enable authentication for all routes

basic_auth = BasicAuth(app)

# Define a route for the root URL
@app.route('/')
def hello():
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
