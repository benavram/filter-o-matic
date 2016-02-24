#!flask/bin/python
from flask import Flask, jsonify
import json
import filteromatic.main
from filteromatic.main import grawlix, replacements 

app = Flask(__name__)
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

def reps():
    return json.dumps(replacements)
    
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    r = reps()
    return jsonify({grawlix})

if __name__ == '__main__':
    app.run(debug=True)