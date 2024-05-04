from flask import Blueprint, request, jsonify
from models import Task, db

tasks_blueprint = Blueprint('tasks', __name__)

# Route để lấy danh sách các công việc
@tasks_blueprint.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = []
    for task in tasks:
        task_list.append({
            'id': task.id,
            'name': task.name,
            'description': task.description,
            'start_date': task.start_date,
            'due_date': task.due_date,
            'category_id': task.category_id,
            'status': task.status
        })
    return jsonify({'tasks': task_list})

# Route để thêm mới một công việc
@tasks_blueprint.route('/tasks/add', methods=['POST'])
def add_task():
    data = request.json
    new_task = Task(
        name=data['name'],
        description=data['description'],
        start_date=data['start_date'],
        due_date=data['due_date'],
        category_id=data['category_id'],
        status=data['status']
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task added successfully'})

# Route để xoá một công việc
@tasks_blueprint.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully'})
    else:
        return jsonify({'message': 'Task not found'}), 404

# Route để cập nhật thông tin của một công việc
@tasks_blueprint.route('/tasks/<int:task_id>/update', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if task:
        data = request.json
        task.name = data['name']
        task.description = data['description']
        task.start_date = data['start_date']
        task.due_date = data['due_date']
        task.category_id = data['category_id']
        task.status = data['status']
        db.session.commit()
        return jsonify({'message': 'Task updated successfully'})
    else:
        return jsonify({'message': 'Task not found'}), 404