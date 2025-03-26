from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Serve your HTML file

@app.route("/api/data")
def get_data():
    return {"key": "value"}  # Example API endpoint

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)