from flask import Flask, jsonify, request

app = Flask(__name__)

# banco de dados simulado

tasks = [
    {
        'id': 1,
        'nome': 'pessoa',
        'done': False
    },
    {
        'id': 2,
        'nome': 'pessoa 2',
        'done': False
    }
]

# obter todas tarefas

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# obter tarefa especifica

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'tarefa não encontrada'}), 404
    return jsonify({'task': task})

# rota para criar uma tarefa nova
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'nome' not in request.json:
        return jsonify({'error': 'A tarefa deve ter um titulo'}), 400

    new_task = {
        'id': tasks[-1]['id'] + 1,
        'nome': request.json['nome'],
        'done': False
    }
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201

# rota para atualizar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Tarefa não encontrada'}), 404

    task['nome'] = request.json.get('nome', task['nome'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify({'task': task})

# rota para deletar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
