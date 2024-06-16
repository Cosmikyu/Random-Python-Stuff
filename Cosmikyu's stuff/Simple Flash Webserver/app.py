from flask import Flask

# Create an instance of Flask
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def hello():
    return "SAS"

@app.route('/about')
def about():
    return "Fuck you, how did you get here??"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)