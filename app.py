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
    return render_template("tasks.html", tasks = tasks) 

@app.route('/details/<task_id>', methods=['GET', 'POST'])
def details(task_id):
    
    for i in data:
        for j in data[i]:
            if task_id == j["id"]:
                
                context = {
                    "task_id" : j["id"],
                    "header" : j["header"],
                    "body" : j["body"],
                    "fields" : list(zip(j["fields"], j["defaults"])),
                    "is_answer" : False,
                    "answer" : "",
                    "chapter" : i
                }

    if request.method == 'POST':
        form = request.form
        d = {i: float(form[i]) if not "/" in form[i] else form[i] for i in form}
        output = call_appropriate_function(task_id, d)
        context["is_answer"] = True
        context["answer"] = output
        return render_template("details.html", **context)
    return render_template("details.html", **context) 

def call_appropriate_function(task_id, context):
    function_list = {
        "1" : f1,
        "2" : f2,
        "3" : f3,
        "4" : f4,
        "5" : f5,
        "6" : f6,
        "7" : f7,
        "8" : f8,
        "9" : f9,
        "10" : f10,
        "11" : f11,
        "12" : f12,
        "13" : f13,
        "14" : f14,
        "15" : f15,
        "16" : f16,
        "17" : f17,
        "18" : f18,
        "19" : f19,
        "20" : f20,
        "21" : f21,
        "22" : f22,
        "23" : f23,
        "24" : f24,
        "25" : f25,
        "26" : f26,
        "27" : f27,
        "28" : f28,
        "29" : f29,
    }

    func = function_list[task_id]
    
    res = func(**context)
    return res
    
if __name__ == '__main__':
    app.run(debug=True)