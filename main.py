 
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/science_explainer")
def science_explainer():
  return render_template("science_explainer.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

if __name__ == "__main__":
  app.run(debug=True)
