import json
from flask import Flask, render_template, request
from chapter1 import *
from chapter2 import *
from chapter3 import *

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

@app.route('/details/<task_id>', methods=['GET', 'POST'])
def details(task_id):
    if request.method == 'POST':
        form = request.form
        for i in form:
            print(i)

    for i in data.values():
        for j in i:
            if task_id == j["id"]:
                context = {
                    "task_id" : j["id"],
                    "header" : j["header"],
                    "body" : j["body"],
                    "fields" : list(zip(j["fields"], j["defaults"]))
                }

    return render_template("details.html", **context) 

def call_appropriate_function(task_id):
    function_list = {
        "1" : f1,
    }

if __name__ == '__main__':
    app.run(debug=True)