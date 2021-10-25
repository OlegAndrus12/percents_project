from flask import Flask, render_template
import json

app = Flask(__name__)

with open("data.json", "r") as f:
    data = json.load(f)
    f.close()


@app.route('/')
def index():
    context = {"text" : "BlaBlaCar", "ids" : [i for i in data]
    }
    
    return render_template("welcome.html", **context)

@app.route('/all')
def all():
    return render_template("tasks.html", data = data)

@app.route('/tasks/<task_id>')
def tasks(task_id):
    return render_template("tasks.html", data = (task_id, data[task_id]))


if __name__ == '__main__':
    app.run(debug=True)