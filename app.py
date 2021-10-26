from flask import Flask, render_template
import json

app = Flask(__name__)

with open("data.json", "r") as f:
    data = json.load(f)
    f.close()


@app.route('/')
@app.route('/index')
def index():
    context = {"text" : "BlaBlaCar", "ids" : [i for i in data]
    }
    return render_template("welcome.html", **context)

@app.route('/all')
def all():
    tasks = list()
    for i in data.values():
        for j in i:
            tasks.append(tuple(j.values()))
    return render_template("tasks.html", tasks = tasks)

@app.route('/tasks/<task_id>')
def tasks(task_id):
    tasks = list()
    for i in data[task_id]:
        tasks.append(tuple(i.values()))
    print(tasks)
    return render_template("tasks.html", tasks = tasks) 

@app.route('/details/<task_id>')
def details(task_id):
    return render_template("details.html")

if __name__ == '__main__':
    app.run(debug=True)