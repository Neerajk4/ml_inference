from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load your Hugging Face model
sentiment_analysis = pipeline("sentiment-analysis")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        result = sentiment_analysis(text)
        return render_template("index.html", result=result[0])
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)