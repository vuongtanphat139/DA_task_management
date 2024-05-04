from flask import Blueprint, request, jsonify
from models import db, Category

categories_blueprint = Blueprint('categories', __name__)

# Endpoint để lấy tất cả các thể loại công việc
@categories_blueprint.route('/categories', methods=['GET'])
def get_all_categories():
    categories = Category.query.all()
    output = []
    for category in categories:
        category_data = {
            'id': category.id,
            'name': category.name,
            'date_created': category.date_created.strftime("%Y-%m-%d")
        }
        output.append(category_data)
    return jsonify({'categories': output})

# Endpoint để thêm một thể loại công việc mới
@categories_blueprint.route('/categories', methods=['POST'])
def add_category():
    data = request.get_json()
    new_category = Category(name=data['name'], date_created=data['date_created'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'New category added successfully!'})

# Endpoint để cập nhật một thể loại công việc
@categories_blueprint.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'error': 'Category not found!'}), 404
    data = request.get_json()
    category.name = data['name']
    category.date_created = data['date_created']
    db.session.commit()
    return jsonify({'message': 'Category updated successfully!'})

# Endpoint để xóa một thể loại công việc
@categories_blueprint.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'error': 'Category not found!'}), 404
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted successfully!'})
