from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    if request.method == "POST":
        try:
            num = int(request.form["number"])
            result = [f"{num} x {i} = {num * i}" for i in range(1, 11)]
        except ValueError:
            result = ["Please enter a valid number."]
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
