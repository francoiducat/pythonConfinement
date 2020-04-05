from flask import Flask, render_template


app = Flask(__name__)

# decorator
@app.route('/')
def home():
    return render_template("home.html")

# decorator
@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)