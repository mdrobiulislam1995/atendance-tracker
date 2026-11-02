from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'attendance_data.json'

default_employees = [
    {"name": "Md Saiful Islam", "mobile": ""},
    {"name": "Md Rabiul Islam", "mobile": ""},
    {"name": "Md Saiful Islam 2", "mobile": ""},
    {"name": "Md Rubel", "mobile": ""},
    {"name": "Md Yasin", "mobile": ""},
    {"name": "Md Riad", "mobile": ""},
    {"name": "Joy", "mobile": ""},
    {"name": "Rakib", "mobile": ""},
    {"name": "Babul", "mobile": ""},
    {"name": "Sourav", "mobile": ""}
]

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "employees": default_employees,
        "records": {},
        "leaves": []
    }

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    data = load_data()
    if request.method == 'POST':
        req_data = request.json
        action = req_data.get('action')
        
        if action == 'update_employees':
            data['employees'] = req_data.get('employees', data['employees'])
            save_data(data)
            return jsonify({"status": "success", "employees": data['employees']})
        
        elif action == 'save_attendance':
            month = req_data.get('month')
            if 'records' not in data:
                data['records'] = {}
            data['records'][month] = req_data.get('records', {})
            save_data(data)
            return jsonify({"status": "success"})
            
        elif action == 'save_leave':
            if 'leaves' not in data:
                data['leaves'] = []
            data['leaves'].append(req_data.get('leave'))
            save_data(data)
            return jsonify({"status": "success"})
            
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
