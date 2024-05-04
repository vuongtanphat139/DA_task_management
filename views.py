from flask import Flask, render_template, request, redirect, url_for

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Route cho trang chủ
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
