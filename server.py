from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("playground.html", boxes = 3, color = "blue")

@app.route('/play/<int:x>')
def boxes(x):
    return render_template("playground.html", boxes = x, color = "blue")

@app.route('/play/<int:x>/<color>')
def boxes_color(x, color):
    return render_template("playground.html", boxes = x, color = color)

if __name__ == "__main__":
    app.run(debug = True)