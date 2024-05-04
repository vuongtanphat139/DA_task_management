from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Cấu hình route để phục vụ các tệp tĩnh từ thư mục static
@app.route('/static/<path:path>')
def serve_static(path):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static'), path)

# Route mặc định hoặc các route khác của ứng dụng Flask
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)