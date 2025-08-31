from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling form submission
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    return f"<h2>Hello, {name}!</h2>"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
