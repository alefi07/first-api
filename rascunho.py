from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados de exemplo (simulando um banco de dados)
tasks = [
    {
        'id': 1,
        'title': 'Estudar Python',
        'done': False
    },
    {
        'id': 2,
        'title': 'Construir uma API',
        'done': False
    }
]

# Rota para obter todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Rota para obter uma tarefa específica
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    return jsonify({'task': task})

# Rota para criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task(): 
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'A tarefa deve ter um título'}), 400

    new_task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'done': False
    }
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201

# Rota para atualizar uma tarefa existente
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Tarefa não encontrada'}), 404

    task['title'] = request.json.get('title', task['title'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify({'task': task})

# Rota para deletar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)

#git