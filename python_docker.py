from flask import Flask
from dotenv import load_dotenv
import os

skills_app = Flask(__name__)


@skills_app.route("/")
def homepage():
    return "Hello From Flask Framework with prod"


@skills_app.route("/about")
def about():
    return "About Page From Flask Framework"


if __name__ == "__main__":
    skills_app.run(debug=True, port=os.getenv(
        "PORT") or 4000, host='0.0.0.0')
