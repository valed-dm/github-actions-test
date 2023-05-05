"""app flask routes"""

from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.get("/", endpoint="index")
def index_view():
    """app index"""
    return render_template("index.html")


@app.get("/about/", endpoint="about")
def about_view():
    """app about"""
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
