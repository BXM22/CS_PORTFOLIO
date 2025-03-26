from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Serve your HTML file

@app.route("/api/data")
def get_data():
    return {"key": "value"}  # Example API endpoint

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    # Send email (use Flask-Mail)
    return "Message sent!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002, debug=True)